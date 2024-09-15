import tkinter as tk
from tkinter import messagebox
from classifier import clasificar_producto
import cv2

# Crear la ventana principal
root = tk.Tk()
root.title("Carrito Inteligente - Retail AI")

# Función para agregar un producto a la lista
def agregar_producto():
    # Simula la captura de una imagen desde la cámara
    imagen = cv2.imread("producto.jpg")  # Reemplaza esto por la captura real
    nombre_producto, precio = clasificar_producto(imagen)
    
    if nombre_producto:
        lista_productos.insert(tk.END, f"{nombre_producto} - ${precio}")
        actualizar_total(precio)
    else:
        alerta_producto_no_detectado()

# Función para actualizar el precio total
total = 0
def actualizar_total(precio):
    global total
    total += precio
    label_total.config(text=f"Total: ${total}")

# Función de alerta para productos no detectados
def alerta_producto_no_detectado():
    messagebox.showwarning("Alerta", "Producto no identificado. Contacte con un asistente.")

# Crear la lista de productos
lista_productos = tk.Listbox(root, height=10, width=50)
lista_productos.pack()

# Botón de agregar producto (simulando la detección de IA)
btn_agregar = tk.Button(root, text="Agregar Producto", command=agregar_producto)
btn_agregar.pack()

# Botón de alerta de producto no detectado
btn_alerta = tk.Button(root, text="Producto No Detectado", command=alerta_producto_no_detectado)
btn_alerta.pack()

# Etiqueta para mostrar el total
label_total = tk.Label(root, text="Total: $0.00", font=("Helvetica", 14))
label_total.pack()

# Ejecutar la ventana
root.mainloop()
