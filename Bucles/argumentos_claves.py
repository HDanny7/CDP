# Argumentos de clave

def saludar(nombre, edad):
    print(f'Muy buenas, {nombre}')
    print(f'Usted tiene {edad} años.')
    
saludar('German', 27)
# Se evitan las complicaciones en la posicion de los argumentos.
saludar(edad = 27, nombre = 'German')


