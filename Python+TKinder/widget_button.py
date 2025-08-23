# Importamos tkinter
import tkinter as tk

# Creacionny config de la ventana
ventana = tk.Tk()
ventana.title('Python: Interfaces graficas.')
ventana.geometry('500x300')

# Botón
boton = tk.Button(text='Haz clic',
                  font=('Arial', 15, 'bold'),
                  background=('pink2'),
                  foreground=('black'),
                  activeforeground=('red2'),
                  activebackground=('blue3'),
                  relief='groove')
boton.pack()

# Bucle para que el programa se mantenga ejecutado
ventana.mainloop()


