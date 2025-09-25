# Importamos tkinter
import tkinter as tk
from tkinter import messagebox as mbox

# Creacion y config de la ventana
ventana = tk.Tk()
ventana.title('Python: Interfaces graficas.')

# Funcion Askinretrycancel
def mostrar_pregunta():
    mbox.askretrycancel('Pregunta', '¿Quieres continuar?') # Muestra una pregunta con opciones Reintentar/Cancelar

'''
# Funcion Askinyesnocancel
def mostrar_pregunta():
    mbox.askyesnocancel('Pregunta', '¿Quieres continuar?') # Muestra una pregunta con opciones Si/No/Cancelar


# Funcion Askinokcancel
def mostrar_pregunta():
    mbox.askokcancel('Pregunta', '¿Quieres continuar?') # Muestra una pregunta con opciones Ok/Cancelar


# Funcion Askyesno
def mostrar_pregunta():
    mbox.askyesno('Pregunta', '¿Quieres continuar?') # Muestra una pregunta con opciones Si/No


# Funcion para mostrar pregunta
def mostrar_pregunta():
    mbox.askquestion('Pregunta', '¿Quien eres?') # Muestra una pregunta
   

# Funcion para mostrar error
def mostrar_error():
    mbox.showerror('Error', '¡Ha ocurrido un error!') # Muestra un mensaje de error


# Funcion para mostrar alerta
def mostrar_alerta():
    mbox.showwarning("Alerta", "¡Cuidado!") # Muestra una alerta de advertencia


# Funcion para mostrar un mensaje
def mostrar_mensaje():
    mbox.showinfo("Información", "¡Hola, mundo!") # Muestra un mensaje de información
'''
# Botón para mostrar el mensaje
boton = tk.Button(ventana, text="Enviar", width=75, command=mostrar_pregunta)
boton.pack()

# Ejecutamos el bucle principal de la ventana
ventana.mainloop()




