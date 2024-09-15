import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz de Usuario - Plan B con Cámara")

# Definir el tamaño de la ventana
root.geometry("800x600")

# Lista de elementos (productos detectados)
lista_productos = tk.Listbox(root, height=10, width=40)
lista_productos.pack(pady=10)

# Campo de entrada para agregar elementos manualmente
entry_producto = tk.Entry(root, width=30)
entry_producto.pack(pady=5)

# Frame donde se mostrará el video en vivo
video_frame = tk.Label(root)
video_frame.pack(pady=10)

# Función para agregar un elemento a la lista manualmente
def agregar_producto():
    producto = entry_producto.get()
    if producto:
        lista_productos.insert(tk.END, producto)
        entry_producto.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, introduce un valor.")

# Función para eliminar el elemento seleccionado
def eliminar_producto():
    try:
        seleccionado = lista_productos.curselection()
        lista_productos.delete(seleccionado)
    except:
        messagebox.showwarning("Error", "Por favor, selecciona un producto.")

# Función para actualizar el elemento seleccionado
def actualizar_producto():
    try:
        seleccionado = lista_productos.curselection()
        producto_nuevo = entry_producto.get()
        if producto_nuevo:
            lista_productos.delete(seleccionado)
            lista_productos.insert(seleccionado, producto_nuevo)
            entry_producto.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, introduce un nuevo valor.")
    except:
        messagebox.showwarning("Error", "Por favor, selecciona un producto.")

# Función para contar los elementos de la lista
def contar_productos():
    cantidad = lista_productos.size()
    messagebox.showinfo("Cantidad de productos", f"Hay {cantidad} productos en la lista.")

# Botones para agregar, eliminar, actualizar y contar elementos
btn_agregar = tk.Button(root, text="Agregar", command=agregar_producto)
btn_agregar.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar", command=eliminar_producto)
btn_eliminar.pack(pady=5)

btn_actualizar = tk.Button(root, text="Actualizar", command=actualizar_producto)
btn_actualizar.pack(pady=5)

btn_contar = tk.Button(root, text="Contar productos", command=contar_productos)
btn_contar.pack(pady=5)

# Función para capturar video en vivo desde la cámara
def iniciar_camara():
    cap = cv2.VideoCapture(0)  # Cámara predeterminada (ID 0)

    def mostrar_video():
        ret, frame = cap.read()  # Leer el cuadro de la cámara
        if ret:
            # Convertir el cuadro a formato que Tkinter pueda manejar (de OpenCV a PIL y luego a ImageTk)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            # Mostrar el video en el frame de video
            video_frame.imgtk = imgtk
            video_frame.configure(image=imgtk)

        # Llamar a la función de nuevo después de 10 ms para actualizar el video
        video_frame.after(10, mostrar_video)

    mostrar_video()

# Iniciar la cámara
iniciar_camara()

# Ejecutar la ventana principal
root.mainloop()

# Al cerrar la ventana, liberar la cámara
cv2.VideoCapture(0).release()
cv2.destroyAllWindows()
