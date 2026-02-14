# Importamos tkinter
import tkinter as tk
import os
from PIL import Image, ImageTk, ImageColor

# Creacion y config de la ventana
ventana = tk.Tk()
ventana.title('Python: Interfaces graficas.')
ventana.geometry('500x300')

# Carpeta donde se encuentran las imagenes
carpeta_imagenes = os.path.dirname(__file__) # obtener el directorio actual del archivo

# cargar directorio de imagenes
imagenes = os.path.join(carpeta_imagenes, 'imagenes') # ruta completa a la carpeta de imagenes, si hubiera otras subcarpetas pondriamos un /, ejemplo(imagenes/otra carpeta).

#Carpeta para fondo
carpeta_fondo = os.path.join(imagenes, 'fondo') # Con este comando se obtiene la ruta completa a la carpeta de fondo.

# Cargar fondo
pintura = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_fondo, 'pintura.jpg')).resize((500, 300))) # Cargar imagen de fondo, resize es un metodo de PIL que redimensiona la imagen a las medidas dadas.

# Creamos una etiqueta
etiqueta = tk.Label(ventana, image=pintura) # Asignamos la imagen a la etiqueta
etiqueta.pack()

# Icono de la ventana
ventana.iconbitmap(os.path.join(imagenes, 'gato.ico')) # Asignamos el icono a la ventana

ventana.mainloop()




