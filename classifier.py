from openvino.runtime import Core
import cv2

# Inicializa OpenVINO
ie = Core()
model_path = "models/model.xml"  # Cambia esto si el modelo está en otro directorio
compiled_model = ie.compile_model(model_path, "CPU")
input_layer = compiled_model.input(0)
output_layer = compiled_model.output(0)

# Función para clasificar un producto
def clasificar_producto(imagen):
    try:
        input_image = cv2.resize(imagen, (224, 224))
        input_image = input_image.transpose((2, 0, 1))
        input_image = input_image.reshape(1, 3, 224, 224)

        # Inferencia
        output = compiled_model([input_image])[output_layer]
        predicted_label = output.argmax()

        # Simula la obtención del nombre del producto y precio
        nombre_producto = f"Producto {predicted_label}"
        precio = 10.99  # Cambia esto por la lógica de la base de datos

        return nombre_producto, precio
    except Exception as e:
        print(f"Error en la clasificación: {e}")
        return None, None
