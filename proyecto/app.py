from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np
import openvino as ov
import torch

app = Flask(__name__)

# Cargar el modelo
with open('class_names.txt', 'r') as file:
    class_names = [line.strip() for line in file.readlines()]

ov_model = ov.convert_model('themodel/themodel', example_input=torch.randn(1, 100, 100, 3))
core = ov.Core()
compiled_model = core.compile_model(ov_model, 'AUTO')

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Función para interpretar el frame y detectar objetos
def contar_objetos():
    ret, frame = cap.read()
    if not ret:
        return 0

    # Procesar el frame
    frame_in = cv2.resize(frame, (100, 100))
    frame_in = cv2.cvtColor(frame_in, cv2.COLOR_BGR2RGB)
    image_array = np.array(frame_in).astype(np.float32)
    image_array = np.expand_dims(image_array, axis=0)

    # Realizar la inferencia
    infer_request = compiled_model.create_infer_request()
    input_tensor = ov.Tensor(image_array)
    infer_request.set_input_tensor(input_tensor)
    infer_request.start_async()
    infer_request.wait()

    # Obtener los resultados
    output = infer_request.get_output_tensor()
    output_buffer = output.data

    # Obtener el nombre del objeto detectado
    objeto_detectado = class_names[np.argmax(np.squeeze(output_buffer))]

    # Devolver el nombre del objeto detectado y el frame para mostrar en el video
    ret, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes(), objeto_detectado

# Función para enviar el stream de video
def generar_video():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_bytes, _ = contar_objetos()

        # Enviar el frame al cliente
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generar_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_object_count', methods=['GET'])
def get_object_count():
    _, objeto_detectado = contar_objetos()
    return jsonify({'count': objeto_detectado})

if __name__ == '__main__':
    app.run(debug=True)
