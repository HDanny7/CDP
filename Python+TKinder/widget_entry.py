# Importamos tkinter
import tkinter as tk

# Creacion y config de la ventana
ventana = tk.Tk()
ventana.title('Python: Interfaces graficas.')
ventana.geometry('500x300')

'''
# Entrada de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Entry y botón
def mostrar_texto():
    texto = entrada.get() # get es un método que obtiene el texto de la entrada, este siempre debe ser llamado.
    tk.Label(ventana, text=texto).pack()

boton = tk.Button(ventana, text='Enviar', command=mostrar_texto)
boton.pack()
'''
# Ejercicio con Insert:
entrada = tk.Entry(ventana)
entrada.insert(0, 'Escribe tu nombre...') # Insert es un método que inserta texto en la entrada, el primer parámetro es la posición (0 es el inicio) y el segundo es el texto.
entrada.bind('<Button-1>', lambda textodelet: entrada.delete(0, tk.END)) # Bind es un método que vincula un evento a un widget, en este caso, al hacer clic (Button-1) en la entrada, se ejecuta una función lambda que borra el texto de la entrada (delete) desde la posición 0 hasta el final (tk.END).
entrada.pack()

# Entry y botón
def mostrar_texto():
    texto = entrada.get() # get es un método que obtiene el texto de la entrada, este siempre debe ser llamado.
    tk.Label(ventana, text=texto).pack()

boton = tk.Button(ventana, text='Enviar', command=mostrar_texto)
boton.pack()
# Bucle para que el programa se mantenga ejecutado
ventana.mainloop()





