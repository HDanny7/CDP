# Importamos tkinter
import tkinter as tk

# Creacionny config de la ventana
ventana = tk.Tk()
ventana.title('Python: Interfaces graficas.')
ventana.geometry('1000x600')

# Crear una fuente
fuente_personalizada = ('Roboto', 15, 'normal')
fuente_personalizada1 = ('Roboto', 15, 'bold')
fuente_personalizada2 = ('Roboto', 15, 'italic')
fuente_personalizada3 = ('Roboto', 15, 'underline')
fuente_personalizada4 = ('Roboto', 15, 'overstrike')

# Etiqueta
etiqueta = tk.Label(text='Hola mundo', 
                    background='lightgreen', 
                    foreground='red',
                    borderwidth=25,
                    cursor='hand2',
                    state='disabled',
                    disabledforeground='blue',
                    font=fuente_personalizada)

# Muestra la eitqueta en la ventana
etiqueta.pack()

# Etiqueta negrilla
etiqueta1 = tk.Label(text='Hola mundo', 
                    background='lightgreen', 
                    foreground='red',
                    borderwidth=25,
                    cursor='hand2',
                    state='disabled',
                    disabledforeground='blue',
                    font=fuente_personalizada1)
etiqueta1.pack()

# Etiqueta cursiva
etiqueta2 = tk.Label(text='Hola mundo', 
                    background='lightgreen', 
                    foreground='red',
                    borderwidth=25,
                    cursor='hand2',
                    state='disabled',
                    disabledforeground='blue',
                    font=fuente_personalizada2)
etiqueta2.pack()

# Etiqueta linea debajo
etiqueta3 = tk.Label(text='Hola mundo', 
                    background='lightgreen', 
                    foreground='red',
                    borderwidth=25,
                    cursor='hand2',
                    state='disabled',
                    disabledforeground='blue',
                    font=fuente_personalizada3)
etiqueta3.pack()

# Etiqueta subrayado
etiqueta4 = tk.Label(text='Hola mundo', 
                    background='lightgreen', 
                    foreground='red',
                    borderwidth=25,
                    cursor='hand2',
                    state='disabled',
                    disabledforeground='blue',
                    font=fuente_personalizada4)
etiqueta4.pack()



# Bucle para que el programa se mantenga ejecutado
ventana.mainloop()


