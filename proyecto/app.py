from flask import Flask, render_template, jsonify
import cv2

app = Flask(__name__)

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Simulación de la detección de objetos
def contar_objetos():
    ret, frame = cap.read()
    if not ret:
        return 0
    
    # Simulación: devolver un número aleatorio de objetos detectados (sustituir con el modelo real)
    objetos_detectados = 5  # Cambiar aquí la lógica por el modelo de visión por computadora
    return objetos_detectados

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_object_count', methods=['GET'])
def get_object_count():
    count = contar_objetos()
    return jsonify({'count': count})

if __name__ == '__main__':
    app.run(debug=True, port = 8000)
