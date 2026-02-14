# Ejemplo de uso de *args y **kwargs en Python

# *args es un parámetro que se utiliza para pasar una cantidad variable de argumentos a una función

def prueba(*args):
    valor = 0
    for i in args:
        valor += 1
        print(f'El argumento numero {valor} es: {i}')

prueba('rojo', 'verde', 'azul')

# **kwargs es un parámetro que se utiliza para pasar una cantidad variable de argumentos con nombre

def claves(**kwargs):
    numero = 0
    for clave in kwargs.keys():
        numero += 1
        print(f'La clave numero {numero} es: {clave} y su valor es: {kwargs[clave]}')
claves(nombre='Juan', edad=30, ciudad='Madrid')