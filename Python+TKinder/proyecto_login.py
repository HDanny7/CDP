# Importamos tkinter
import tkinter as tk
import os
from PIL import Image, ImageTk, ImageColor
import getpass # Importamos getpass para ocultar la contraseña en la consola

# Creacion y config de la ventana
ventana = tk.Tk()
ventana.title('Bella Durmiente.')

# Creación de usuario y contraseña
usuario_creado = ()

while True: # Bucle para crear usuario y contraseña
    nuevo_usuario = input('Introduce un nuevo usuario:\n') # Creación de nuevo usuario
    nueva_contrasena = getpass.getpass('Introduce una nueva contraseña:\n') # Creación de nueva contraseña y ocultación en la consola
    repite_usuario = input('Repite el usuario nuevamente:\n') # Confirmación de usuario
    repite_contrasena = getpass.getpass('Repite la contraseña nuevamente:\n') # Confirmación de contraseña

    if nuevo_usuario != repite_usuario or nueva_contrasena != repite_contrasena: # Comprobación de usuario y contraseña
        print('Los datos no coinciden. Inténtalo de nuevo.')
    else:
        usuario_creado = (nuevo_usuario, nueva_contrasena) # Si los datos coinciden, se guarda el usuario y la contraseña
        print('Usuario y contraseña creados correctamente.')
        break

# Carpeta donde se encuentran las imagenes
carpeta_imagenes = os.path.dirname(__file__) # obtener el directorio actual del archivo

# cargar directorio de imagenes
imagenes = os.path.join(carpeta_imagenes, 'imagenes') # ruta completa a la carpeta de imagenes, si hubiera otras subcarpetas pondriamos un /, ejemplo(imagenes/otra carpeta).

#Carpeta para fondo
carpeta_imag = os.path.join(imagenes, 'fondo') # Con este comando se obtiene la ruta completa a la carpeta de fondo.

# Icono de la ventana
ventana.iconbitmap(os.path.join(imagenes, 'pies.ico')) # Asignamos el icono a la ventana

# Imagen de fondo
imagen = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imag, 'durm.png')).resize((500, 350))) # Con este comando se obtiene la ruta completa a la imagen.
muestra_imagen = tk.Label(image=imagen)
muestra_imagen.pack()

# Etiquetas usuario y contraseña
etiqueta_usuario = tk.Label(ventana, text='Usuario:')
etiqueta_usuario.pack()
# Entrada usuario
entrada_usuario = tk.Entry(ventana)
entrada_usuario.insert(0, 'Usuario..')
entrada_usuario.bind('<Button-1>', lambda textodelet: entrada_usuario.delete(0, tk.END))
entrada_usuario.pack()

etiqueta_contrasena = tk.Label(ventana, text='Contraseña:')
etiqueta_contrasena.pack()
# Entrada contraseña
entrada_contrasena = tk.Entry(ventana, show='*')
entrada_contrasena.insert(0, '*'*7)
entrada_contrasena.bind('<Button-1>', lambda textodelet: entrada_contrasena.delete(0, tk.END))
entrada_contrasena.pack()

# Creación de la función para verificar usuario y contraseña
def validar():
    usuario = entrada_usuario.get() # get es un método que obtiene el texto de la entrada, este siempre debe ser llamado.
    contrasena = entrada_contrasena.get()
    if usuario != usuario_creado[0] or contrasena != usuario_creado[1]: # Comprobación de usuario y contraseña
        tk.Label(text='Usuario o contraseña incorrectos. Inténtalo de nuevo.', fg='red').pack()
    else:
        tk.Label(text=f'Hola, {usuario_creado[0]}. Espere unos instantes...', fg='green').pack()


# Botón para enviar
boton = tk.Button(ventana, text='Entrar', command=validar) # command es un parámetro que asigna una función al botón, en este caso, la función validar.
boton.pack()

# Bucle de la ventana
ventana.mainloop()


