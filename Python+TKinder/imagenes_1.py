# Importamos tkinter
import tkinter as tk
import os
from PIL import Image, ImageTk, ImageColor

# Creacion y config de la ventana
ventana = tk.Tk()
ventana.title('Python: Interfaces graficas.')

# Carpeta donde se encuentran las imagenes
carpeta_imagenes = os.path.dirname(__file__) # obtener el directorio actual del archivo

# cargar directorio de imagenes
imagenes = os.path.join(carpeta_imagenes, 'imagenes') # ruta completa a la carpeta de imagenes, si hubiera otras subcarpetas pondriamos un /, ejemplo(imagenes/otra carpeta).

#Carpeta para fondo
carpeta_imag = os.path.join(imagenes, 'imag') # Con este comando se obtiene la ruta completa a la carpeta de fondo.

#Crear una lista con las imagenes
lista_imagenes = ['imagen_1.jpg', 'imagen_2.jpg', 'imagen_3.jpg', 'imagen_4.jpg']

# Imagen 1
imagen_0 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imag, f'{lista_imagenes[0]}')).resize((400, 250))) # Con este comando se obtiene la ruta completa a la imagen.
muestra_imagen_0 = tk.Label(image=imagen_0)
muestra_imagen_0.grid(row=0, column=0)

# Imagen 2
imagen_1 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imag, f'{lista_imagenes[1]}')).resize((400, 250))) # Con este comando se obtiene la ruta completa a la imagen.
muestra_imagen_1 = tk.Label(image=imagen_1)
muestra_imagen_1.grid(row=1, column=0)

# Imagen 3
imagen_2 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imag, f'{lista_imagenes[2]}')).resize((400, 250))) # Con este comando se obtiene la ruta completa a la imagen.
muestra_imagen_2 = tk.Label(image=imagen_2)
muestra_imagen_2.grid(row=0, column=1)

# Imagen 4
imagen_3 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imag, f'{lista_imagenes[3]}')).resize((400, 250))) # Con este comando se obtiene la ruta completa a la imagen.
muestra_imagen_3 = tk.Label(image=imagen_3)
muestra_imagen_3.grid(row=1, column=1)

# Icono de la ventana
ventana.iconbitmap(os.path.join(imagenes, 'pies.ico')) # Asignamos el icono a la ventana

# Bucle de la ventana
ventana.mainloop()
