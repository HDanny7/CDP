# Importamos tkinter
import tkinter as tk

# Creacionny config de la ventana
ventana = tk.Tk()
ventana.title('Python: Interfaces graficas.')
ventana.geometry('500x300')

# Creacion de las etiquetas
mensaje1 = tk.Label(ventana, text='Hola Mundo')
mensaje2 = tk.Label(ventana, text='Adios Mundo')
# Con pack lo que hacemos es mostrar las etiquetas pero por defecto aparecen en el centro.
'''
mensaje1.pack()
mensaje2.pack()'''
# Con grid lo que hacemos es mostrar las etiquetas en una cuadrícula.
# Estas se separan por columnas y filas que vienen establecidas por defecto.
mensaje1.grid(row=0, column=0)
mensaje2.grid(row=1, column=0)
ventana.mainloop()