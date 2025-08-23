# Hay diferentes modulos, algunos que se pueden importar y tros que ya estan incluidos en python
# Para usar algo del modulo importado hay que nombrarlo y poner un punto con el elemento a utilizar

'''import random
# Generar un numero aleatorio entre 1 y 1000
aleatorio = random.randint(1, 1000)
print(aleatorio)'''

# funcion dir: Devuelve una lista con los nombres definidos de una lista de nombres.
# Se puede cargar una parte de otro modulo con from.
'''from random import randint
aleatorio = randint(1, 1000)
print(aleatorio)'''

# Importar todos los elementos 'No muy recomendado'
'''from random import *
aleatorio = randint(1, 1000)'''
# No se permiten la importancion con * dentro de una funcion o clase.
# Importacion de multiples modulos.
'''import math
import random'''
# Importaciones con alias
import random as rd
aleatorio = rd.randint(1, 1000)
print(aleatorio)





