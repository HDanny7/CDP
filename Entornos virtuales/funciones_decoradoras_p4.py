'''def a(b):
    def c(*args):
        print('El resultado de la operacion es:')
        b(*args)
        print('Operacion realizada con éxito.')
    return c

@a    
def sumar(num1, num2):
    print(num1 + num2)

sumar(40, 54)
sumar(100, 305)
sumar(48, 52)

@a
def restar(num1, num2, num3, num4):
    print(num1 - num - num3 - num4)

restar(40, 54, 60, 43)'''

import math
def a(b):
    def c(*args, **kwargs): # laidea de poner el **kwargs es para que la funcion pueda recibir asi mismo argumentos posicionales como *arg y de clave con **kwargs.
        print('Empieza el calculo.')
        b(*args, **kwargs)
        print('Operacion realizada con exito.')
    return c
@a
def area_rectangulo(base, altura):
    print(f'El area del rectagulo es:{base * altura}.')
@a
def area_triangulo(base, altura):
    print(f'El area del triangulo es: {base * altura / 2}.')
@a
def area_circulo(radio):
    print(f'El area del circulo es: {math.pi * radio **2}.')

area_rectangulo(10, 40)






