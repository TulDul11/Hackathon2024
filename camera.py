import cv2

def capturar_imagen():
    # Iniciar la cámara
    cap = cv2.VideoCapture(0)  # 0 es para la cámara predeterminada

    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return None

    ret, frame = cap.read()
    if ret:
        cv2.imwrite("producto.jpg", frame)  # Guarda la imagen capturada
        return frame
    else:
        print("Error: No se pudo capturar la imagen.")
        return None
