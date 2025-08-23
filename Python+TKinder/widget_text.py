# Importamos tkinter
import tkinter as tk

# Creacionny config de la ventana
ventana = tk.Tk()
ventana.title('Python: Interfaces graficas.')
ventana.geometry('500x300')

# 1
# Widget Text
'''
texto = tk.Text(ventana,
                background='tan1',
                font=('Calibri', 14),
                foreground='DarkOliveGreen4',
                cursor='pencil')
texto.pack()
'''
# 2
'''
# Contador de texto ( para que cuente cuantas lineas de texto se genera)
contador = 0

# Widget Text
texto = tk.Text(ventana, width=50, height=15)
texto.pack()

# Insert text
def insetar_texto():
    global contador
    contador +=1
    texto.insert(tk.END, f'¡Linea {contador}!\n')

# Boton para insertar la funcion de inserción de texto
boton_insertar = tk.Button(ventana, text='Insertar texto', command= insetar_texto)
boton_insertar.pack()

# Bucle principal
ventana.mainloop()
'''
# 3
'''
# Widget Text
texto = tk.Text(ventana, width=50, height=15)
texto.pack()

# Elimminar texto
# Insertams texto
texto.insert('1.0', 'Primera línea.\n')
texto.insert('2.0', 'Primera línea.\n')
texto.insert('3.0', 'Primera línea.\n')

# Función para eliminar texto
def eliminar_texto():
    texto.delete('1.0', tk.END)

# Botón para añadir la funcion de eliminar texto
boton_eliminar = tk.Button(ventana, text='Eliminar texto', command=eliminar_texto)
boton_eliminar.pack()

# Bucle principal
ventana.mainloop()
'''

# 4
'''
# Widget Text
texto = tk.Text(ventana, width=50, height=15)
texto.pack()


# Obtener texto
def obtener_texto():
    texto_obtenido = texto.get('1.0', 'end')
    print(texto_obtenido)

# Botón para añadir la funcion de eliminar texto
boton_obtener = tk.Button(ventana, text='Obtener texto', command=obtener_texto)
boton_obtener.pack()

# Seleccionar texto
def obtener_texto():
    seleccion = texto.get('sel.first', 'sel.last')
    print('Texto seleccionado:', seleccion)

# Botón para añadir la funcion de eliminar texto
boton_obtener = tk.Button(ventana, text='Obtener seleccion', command=obtener_texto)
boton_obtener.pack()

# Bucle principal
ventana.mainloop()'''

# 5
'''
# Reemplazar texto

# Widget Text
texto = tk.Text(ventana, width=50, height=15)
texto.pack()

# Funcion para modificar texto
def modificar_seleccion():
    nuevo_texto = '¡TEXTO MODIFICADO!'
    texto.replace('sel.first', 'sel.last', nuevo_texto)

# Botón para modificar seleccion
boton_modificar_seleccion = tk.Button(ventana, text='Modificar seleccion', command=modificar_seleccion)
boton_modificar_seleccion.pack()

# Bucle principal
ventana.mainloop()
'''

# 6
# Obtener la posicion del cursor

# Widget Text
texto = tk.Text(ventana, width=50, height=15)
texto.pack()

# Funcion para posicion del cursor
def posicion_cursor(evento):
    posicion = texto.index(tk.CURRENT) # Se puede usar INSERT o CURRENT
    print('Posicion del curso:', posicion)

# Asociar las pulsaciones de teclas a la funcion
texto.bind('<KeyRelease>', posicion_cursor) # Se puede usar Key o KeyRelease

# Bucle principal
ventana.mainloop()




