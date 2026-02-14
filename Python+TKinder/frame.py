# Importamos tkinter
import tkinter as tk

# Creacion y config de la ventana
ventana = tk.Tk()
ventana.title('Python: Interfaces graficas.')

'''
# Creamos un marco
marco_1 = tk.LabelFrame(ventana, text='Marco de la ventana principal', 
                      padx=15, pady=15,)
marco_1.pack(padx=10, pady=10)

marco_2 = tk.LabelFrame(ventana, text='Enviar', 
                      padx=15, pady=15,)
marco_2.pack(padx=10, pady=10)

marco_3 = tk.LabelFrame(ventana, text='Resultado', 
                      padx=15, pady=15,)
marco_3.pack(padx=10, pady=10)

# Entrada de datos
entrada = tk.Entry(marco_1,
                     font=('Arial', 18),
                     fg='blue',
                     bg='spring green',
                     border=5,
                     width=30)
entrada.pack()
entrada.insert(0, 'Escribe nombre...')
entrada.bind('<Button-1>', lambda event: entrada.delete(0, tk.END))

# Funcion para el boton
def enviar():
    nombre = entrada.get()
    tk.Label(marco_3, text=f'Hola {nombre}', 
             font=('Arial', 18), 
             fg='blue', 
             width=27).pack()
    entrada.delete(0, tk.END)
    entrada.insert(0, 'Escribe nombre...')

# Boton de enviar
boton = tk.Button(marco_2, text='Enviar', 
                  command=enviar, 
                  bg='deepskyblue', 
                  border=3, 
                  width=26).pack()

'''
# Con Grid ajustamos en donde sale el marco espacialmente.

# Creamos un marco
marco_1 = tk.LabelFrame(ventana, text='Marco de la ventana principal', 
                      padx=15, pady=15,)
marco_1.grid(row=0, column=0, padx=10, pady=10)

marco_2 = tk.LabelFrame(ventana, text='Enviar', 
                      padx=15, pady=15,)
marco_2.grid(row=1, column=0, padx=10, pady=10)

marco_3 = tk.LabelFrame(ventana, text='Resultado', 
                      padx=15, pady=15,)
marco_3.grid(row=0, column=1, padx=10, pady=10)

# Entrada de datos
entrada = tk.Entry(marco_1,
                     font=('Arial', 18),
                     fg='blue',
                     bg='spring green',
                     border=5,
                     width=30)
entrada.pack()
entrada.insert(0, 'Escribe nombre...')
entrada.bind('<Button-1>', lambda event: entrada.delete(0, tk.END))

# Funcion para el boton
def enviar():
    nombre = entrada.get()
    tk.Label(marco_3, text=f'Hola {nombre}', 
             font=('Arial', 18), 
             fg='blue', 
             width=27).pack()
    entrada.delete(0, tk.END)
    entrada.insert(0, 'Escribe nombre...')

# Boton de enviar
boton = tk.Button(marco_2, text='Enviar', 
                  command=enviar, 
                  bg='deepskyblue', 
                  border=3, 
                  width=26).pack()

ventana.mainloop()
