# Importamos tkinter
import tkinter as tk

# Creacion y config de la ventana
ventana = tk.Tk()
ventana.title('Python: Interfaces graficas.')

# Variable de control tipo Intvar
opcion = tk.IntVar()

# Establecer un valor por defecto
opcion.set(1)

# Funcion para mostrar la opcion seleccionada
def actualiza_radio(valor):
    tk.Label(ventana, text=valor).pack()

# Creamos un RadioButton

tk.Radiobutton(ventana, text='Rojo', variable=opcion, value=1).pack()

tk.Radiobutton(ventana, text='Verde', variable=opcion, value=2).pack()

tk.Radiobutton(ventana, text='Azul', variable=opcion, value=3).pack()

# Boton de envio
tk.Button(ventana, text='Enviar', command=lambda: actualiza_radio(opcion.get())).pack()

ventana.mainloop()



