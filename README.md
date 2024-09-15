# Hackathon2024
ACM Hackathon 2024 - Softtek Challenge

# Carfield: Carrito Inteligente - Detección de Objetos en Tiempo Real

Este proyecto es una aplicación de visión por computadora para la detección de objetos en tiempo real, utilizando cámaras integradas en un carrito inteligente. La aplicación está construida en **Python** y utiliza varias bibliotecas de visión por computadora y aprendizaje profundo, incluyendo **OpenVINO**, **OpenCV**, **Flask** y **TensorFlow**.

## Requisitos previos

Antes de ejecutar la aplicación, asegúrate de que tienes instaladas las siguientes herramientas:

### 1. **Python 3.x**
   - La aplicación está escrita en Python, por lo que necesitas tener instalado **Python 3.x**.
   - Puedes descargar Python desde [aquí](https://www.python.org/downloads/).

### 2. **Librerías necesarias**
   Necesitarás instalar las siguientes librerías en tu entorno de desarrollo:

   - **Flask**: Para el desarrollo del servidor web.
   - **OpenVINO**: Para la optimización y ejecución del modelo de detección de objetos.
   - **OpenCV**: Para la captura de video y procesamiento de imágenes.
   - **TensorFlow**: Para manejar modelos de aprendizaje profundo.
   
   Para instalarlas, sigue los pasos descritos en la sección de instalación.

## Instalación

### 1. Clonar el repositorio
   Si no lo has hecho ya, clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-repo/carfield-carrito-inteligente.git
   cd carfield-carrito-inteligente
   ```

### 2. Crear un entorno virtual (opcional, pero recomendado)

   Para evitar conflictos con otras instalaciones de Python en tu sistema, se recomienda crear un **entorno virtual**:

   ```bash
   python -m venv venv
   ```

   Luego, activa el entorno virtual:

   - En **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - En **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

### 3. Instalar las dependencias

   Una vez dentro del entorno virtual, instala las librerías necesarias ejecutando el siguiente comando:

   ```bash
   pip install flask opencv-python openvino tensorflow
   ```

   Aquí está un desglose de las librerías:

   - **Flask**: Proporciona un marco de trabajo para crear el servidor web.
   - **OpenCV**: Maneja la captura de video de la cámara y el procesamiento de imágenes.
   - **OpenVINO**: Permite la optimización y la inferencia del modelo de IA.
   - **TensorFlow**: Proporciona la base para el modelo de aprendizaje profundo.

### 4. Descargar el modelo preentrenado

   Asegúrate de que tienes el modelo preentrenado que estás usando para la detección de objetos. Colócalo en la carpeta especificada dentro del código `app.py`.

   ```bash
   themodel/themodel
   ```

## Uso

### 1. Ejecutar la aplicación

   Una vez que hayas instalado todas las dependencias, puedes ejecutar la aplicación **`app.py`** desde la terminal.

   Ejecuta el siguiente comando:

   ```bash
   python app.py
   ```

   Deberías ver algo como esto en la terminal:

   ```
   * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
   ```

   Esto indica que el servidor Flask está en funcionamiento y que la aplicación está accesible en `localhost`.

### 2. Abrir en el navegador

   Abre tu navegador web favorito y ve a la siguiente URL:

   ```
   http://127.0.0.1:8000/
   ```

   Verás la interfaz del **Carrito Inteligente**, con el video en tiempo real de la cámara y el conteo de los objetos detectados.

### 3. Detener la aplicación

   Para detener la aplicación, ve a la terminal donde está corriendo y presiona **CTRL + C**.

## Estructura del proyecto

```
carfield-carrito-inteligente/
│
├── app.py               # Archivo principal de la aplicación Flask
├── templates/
│   └── index.html       # Archivo HTML de la interfaz de usuario
├── static/
│   ├── styles.css       # Archivo de estilos CSS
│   └── logo.png         # Logo del programa
├── themodel/
│   └── themodel         # Carpeta donde se guarda el modelo preentrenado
└── class_names.txt      # Lista de nombres de las clases detectadas
```

## Funcionalidades

- **Detección de objetos en tiempo real**: El sistema utiliza la cámara integrada para capturar el video en vivo y procesar cada fotograma utilizando el modelo de visión por computadora.
- **Conteo de objetos detectados**: La UI muestra un contador que se actualiza en tiempo real con el número de objetos detectados.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de hacer un **fork** del repositorio, realizar los cambios necesarios y enviar un **pull request**.

---

Si tienes preguntas o problemas al ejecutar la aplicación, no dudes en crear un **issue** en el repositorio.
