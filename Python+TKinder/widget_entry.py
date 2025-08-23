# Importamos tkinter
import tkinter as tk

# Creacionny config de la ventana
ventana = tk.Tk()
ventana.title('Python: Interfaces graficas.')
ventana.geometry('500x300')

# Entrada de texto
entrada = tk.Entry(ventana)

entrada.pack()

# Bucle para que el programa se mantenga ejecutado
ventana.mainloop()





