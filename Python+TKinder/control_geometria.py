# Importamos tkinter
import tkinter as tk

# Ventana
ventana = tk.Tk()
ventana.title('Python: Interfaces graficas')
'''
# Configura la geometria de l aventana
ventana.geometry('400x75+40+70')

ventana.mainloop()
'''
# 2 Centrar ventanas dinamicas

# Obtener el ancho y el alto de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Imprimir dimenciones de la pantalla
print(f'Ancho de la pantalla: {ancho_pantalla} pixeles')
print(f'Alto de la pantalla: {alto_pantalla} pixeles')

# Establece el tamaño de la ventana
ancho_ventana = 500
alto_ventana = 300

# Calcula la posicion x e y para centrar la ventana
posicion_x = round(ancho_pantalla / 2 - ancho_ventana / 2)
posicion_y = round( alto_pantalla / 2 - alto_ventana / 2)

# Imprimir posiciones calculadas
print(f'Posicion X para centrar la ventana: {posicion_x} pixeles')
print(f'Posicion Y para centrar la ventana: {posicion_y} pixeles')

# Configuracion geometrica de l aventana
ventana.geometry(f'{ancho_pantalla}x{alto_ventana}+{posicion_x}+{posicion_y}')

ventana.mainloop()







