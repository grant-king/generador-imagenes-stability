### generador-imagenes-stability
Aplicación para generar imágenes utilizando la API de Stability con una interfaz amigable.

# Generación de Imágenes con Stability - Demo

Este proyecto demuestra una aplicación sencilla para generar imágenes utilizando la API de Stability, aprovechando la biblioteca Gradio para una interfaz de usuario amigable.

## Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Prerrequisitos](#prerrequisitos)
- [Instalación](#instalación)
- [Ejecución de la Aplicación](#ejecución-de-la-aplicación)
- [Uso](#uso)
- [Estructura de la Aplicación](#estructura-de-la-aplicación)
- [Notas Importantes](#notas-importantes)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Descripción General

Esta aplicación de demostración permite a los usuarios generar imágenes utilizando prompts de texto a través de la API de Stability. Cuenta con una interfaz gráfica creada con Gradio para hacer que el proceso de generación sea sencillo e interactivo.

Los componentes principales del proyecto incluyen:

- **AdministradorGenerador**: Maneja las llamadas a la API para generar imágenes.
- **GeneradorRespuesta**: Procesa y guarda las respuestas de la API de Stability.
- **Interfaz Gradio**: Proporciona una interfaz web amigable para ingresar prompts y ver las imágenes generadas.

## Prerrequisitos

Antes de ejecutar la aplicación, asegúrate de tener instalado lo siguiente:

- Python 3.8 o superior
- [Pip](https://pip.pypa.io/en/stable/installation/)
- Clave API de [Stability AI](https://stability.ai/), que debe ser guardada en un archivo `.env`.

Tu archivo `.env` debe incluir:

```env
STABILITY_API_KEY=tu_clave_api_de_stability_aquí
```

## Instalación

Para comenzar, sigue estos pasos para configurar tu entorno:

1. Clona el repositorio en tu máquina local:

   ```bash
   git clone https://github.com/grant-king/stability_demo.git
   cd stability_demo
   ```

2. Crea un entorno virtual y actívalo:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows, usa `venv\Scripts\activate`
   ```

3. Instala los paquetes necesarios:

   ```bash
   pip install -r requirements.txt
   ```

4. Crea un archivo `.env` en el directorio raíz y añade tu clave API de Stability:

   ```bash
   echo "STABILITY_API_KEY=tu_clave_api_de_stability_aquí" > .env
   ```

## Ejecución de la Aplicación

Para lanzar la aplicación, simplemente ejecuta:

```bash
python stability_demo/app_demo_2.py
```

La aplicación iniciará una interfaz web de Gradio con la que puedes interactuar a través de tu navegador en la dirección local proporcionada.

## Uso

1. **Ingresa tu Prompt**: Escribe un prompt de texto describiendo la imagen que deseas generar.
2. **Selecciona Relación de Aspecto**: Elige una relación de aspecto para la imagen generada. Las opciones disponibles incluyen "1:1", "16:9", "9:16", etc.
3. **Generar**: Haz clic en el botón "Generar" para crear una imagen. La imagen generada se mostrará abajo, y puedes ver una galería de todas tus imágenes generadas.

Las imágenes se guardan localmente en la carpeta `imagenes_generadas`.

## Estructura de la Aplicación

- `app_demo_2.py`: Script principal que incluye las clases `AdministradorGenerador` y `GeneradorRespuesta` para interactuar con la API de Stability y la interfaz Gradio para la interacción del usuario.

### Componentes Clave

- **AdministradorGenerador**: Esta clase es responsable de realizar solicitudes a la API de Stability y guardar las respuestas.

  - `__init__()`: Inicializa la clave API, la URL base y el directorio de salida.
  - `generar_imagen()`: Envía una solicitud a la API de Stability utilizando un prompt dado y devuelve un objeto `GeneradorRespuesta`.

- **GeneradorRespuesta**: Maneja la respuesta de la API y guarda la imagen.

  - `__init__()`: Procesa la respuesta de la API y guarda la imagen generada en un archivo si tiene éxito.
  - `image()`: Devuelve la ruta de la imagen guardada, que Gradio utiliza para mostrarla.

## Notas Importantes

- **Variables de Entorno**: La clave API se accede a través de variables de entorno por seguridad. Asegúrate de que el archivo `.env` esté configurado correctamente antes de ejecutar el script.
- **API de Stability**: Esta demo utiliza la API de Stability AI, específicamente apuntando a un endpoint del modelo para generación de imágenes. Asegúrate de que tu clave API sea válida y tenga los permisos correctos.
- **Interfaz Gradio**: Gradio proporciona una forma interactiva para que los usuarios ingresen prompts de texto y vean resultados. La función de galería mantiene un historial de imágenes generadas durante la sesión.

## Contribuciones

¡Las contribuciones son bienvenidas! No dudes en bifurcar el repositorio y enviar pull requests para mejoras.

## Licencia

Este proyecto está bajo la Licencia Unlicense. Consulta el archivo LICENSE para más información.

## Contacto

Para preguntas o soporte, por favor abre un issue en el repositorio de GitHub o contáctanos en `g@grantking.dev`.

---

¡Feliz spinning!
