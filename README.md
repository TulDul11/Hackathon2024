# Carrito Inteligente - Proyecto de Hackathon

Este es un proyecto de carro de supermercado inteligente, usando OpenVINO para la detección de productos y una interfaz de usuario en Python.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-repositorio/carro-inteligente.git
    cd carro-inteligente
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

3. Configura OpenVINO en tu entorno:
    - En Linux/macOS:
      ```bash
      source /opt/intel/openvino/setupvars.sh
      ```
    - En Windows:
      ```bash
      "C:\Program Files (x86)\Intel\openvino\bin\setupvars.bat"
      ```

4. Ejecuta la interfaz de usuario:
    ```bash
    python src/ui.py
    ```

## Uso
- Usa el botón "Agregar Producto" para simular la detección de un producto con la IA.
- Si no se detecta correctamente, el sistema mostrará una alerta.
