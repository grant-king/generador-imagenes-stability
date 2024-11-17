# Importamos las librerías necesarias
import requests  # Para hacer solicitudes HTTP
import os  # Para acceder a variables de entorno y funcionalidades del sistema operativo
from dotenv import load_dotenv  # Para cargar variables de entorno desde un archivo .env
from datetime import datetime  # Para manejar fechas y horas
from pathlib import Path  # Para manipular rutas de archivos y directorios
import gradio as gr  # Para crear interfaces gráficas de usuario

load_dotenv()  # Cargamos las variables de entorno desde el archivo .env

class AdministradorGenerador:
    """
    Una clase para manejar la generación de imágenes usando la API de Stability.
    Atributos:
        clave_api (str): La clave API para acceder a la API de Stability.
        url_base (str): La URL base para la API de Stability.
        apendice_modelo (str): El complemento de modelo para el endpoint de la API.
        respuestas (list): Una lista para almacenar las respuestas de la API.
        directorio_salida (Path): El directorio donde se guardarán las imágenes generadas.
    Métodos:
        generar_imagen(prompt, relacion_aspecto="1:1"):
            Genera una imagen basada en el prompt y la relación de aspecto proporcionados.
            Args:
                prompt (str): El texto prompt para generar la imagen.
                relacion_aspecto (str): La relación de aspecto de la imagen generada. Por defecto es "1:1".
            Returns:
                GeneradorRespuesta: El objeto de respuesta que contiene la imagen generada y metadatos.
    """
    def __init__(self, directorio_salida="imagenes_generadas"):
        self.clave_api = os.getenv("STABILITY_API_KEY")
        self.url_base = "https://api.stability.ai/v2beta/stable-image"
        self.apendice_modelo = "core"
        self.respuestas = []
        
        # Creamos el directorio de salida si no existe
        self.directorio_salida = Path(directorio_salida)
        self.directorio_salida.mkdir(exist_ok=True)

    def generar_imagen(self, prompt, relacion_aspecto="1:1"):
        encabezados = {
            "Accept": "image/*",  # Solicitamos una respuesta directa de imagen
            "Authorization": f"Bearer {self.clave_api}",
        }

        archivos = {
            "prompt": (None, prompt),
            "aspect_ratio": (None, relacion_aspecto),
            "output_format": (None, "png"),  # Solicitamos explícitamente el formato PNG
        }

        host = f'{self.url_base}/generate/{self.apendice_modelo}'
        
        # Realizamos la solicitud
        respuesta_servicio = requests.post(
            host,
            headers=encabezados,
            files=archivos,
        )
        
        respuesta = GeneradorRespuesta(respuesta_servicio, self.directorio_salida)
        self.respuestas.append(respuesta)
        return respuesta

class GeneradorRespuesta:
    """
    Una clase para manejar la respuesta de un servicio y guardar el contenido de la imagen en un directorio especificado.
    Atributos:
        codigo_estado (int): El código de estado HTTP de la respuesta del servicio.
        razon_finalizacion (str): La razón de finalización de la respuesta del servicio.
        ruta_imagen (Path o None): La ruta donde se guarda la imagen, o None si la imagen no se guardó.
    Métodos:
        __init__(respuesta_servicio, directorio_salida):
            Inicializa GeneradorRespuesta con la respuesta del servicio y el directorio de salida.
            Guarda el contenido de la imagen en el directorio especificado si la respuesta es exitosa.
        image:
            Devuelve la ruta de la imagen guardada como una cadena para que Gradio la muestre, o None si la imagen no se guardó.
    """
    def __init__(self, respuesta_servicio, directorio_salida):
        self.codigo_estado = respuesta_servicio.status_code
        self.razon_finalizacion = respuesta_servicio.headers.get('finish_reason')
        self.ruta_imagen = None
        
        if self.codigo_estado != 200:
            print(f'Error: {respuesta_servicio.content}')
            return
        
        # Generamos un nombre de archivo único usando la marca de tiempo
        marca_tiempo = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"estabilidad_{marca_tiempo}.png"
        self.ruta_imagen = directorio_salida / nombre_archivo
        
        # Guardamos la imagen directamente desde el contenido de la respuesta
        with open(self.ruta_imagen, 'wb') as f:
            f.write(respuesta_servicio.content)

    @property
    def image(self):
        """Devuelve la ruta de la imagen guardada para que Gradio la muestre"""
        return str(self.ruta_imagen) if self.ruta_imagen else None

gen_manager = AdministradorGenerador()

def generar_imagen_desde_prompt(prompt, relacion_aspecto, galeria):
    resultado = gen_manager.generar_imagen(prompt, relacion_aspecto)
    if resultado.codigo_estado == 200:
        galeria = galeria or []
        galeria.append(resultado.image)
        return resultado.image, galeria, galeria
    else:
        return None, galeria, galeria

def main():
    with gr.Blocks() as interfaz:
        with gr.Column():
            with gr.Row():
                prompt = gr.Textbox(label="Ingresa tu prompt")
                relacion_aspecto = gr.Dropdown(
                    choices=["1:1", "16:9", "9:16", "4:5", "5:4", "3:2", "2:3", "9:21", "21:9"],
                    value="1:1",
                    label="Relación de Aspecto"
                )
            boton_generar = gr.Button("Generar")
            with gr.Row():
                vista_previa = gr.Image(label="Última Generación")
            with gr.Row():
                galeria = gr.Gallery(label="Historial de Generaciones")
        
        estado_galeria = gr.State([])

        boton_generar.click(
            fn=generar_imagen_desde_prompt,
            inputs=[prompt, relacion_aspecto, estado_galeria],
            outputs=[vista_previa, galeria, estado_galeria]
        )
    
    interfaz.launch()

if __name__ == "__main__":
    main()
