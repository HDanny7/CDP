# Alcance o Ambito
'''Diferentes elementos crean alcance en python, Modulo, clase, funciones(def y lambda),
compresiones(list, set y dict), expresiones generadoras.
'''
'''Namespace: Son contenedores de identificadores unicos que permiten organizar el codigo en areas,
evitando conflictos de areas.'''

'''def imprimir_nombre(): # Variable Global
    nombre = 'Germán' Local scape
    print(nombre)
imprimir_nombre()

def funcion():
    a = 10
    b = 'Hola'
    c = 10.56
    print(locals)
funcion()'''

# Funcion predefinida VARS: devuelve el atributo dict(Imprime los diccionarios de la clase o lo que sea que tengamos.)
'''class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
usuario1 = Usuario('Ger', ' Carrs', 27)
usuario2 = Usuario('Dan', 'Col', 27)

# Definicion de un atributo diferente a cada objeto
usuario1.correo = 'nr7german@gmail.com'
usuario2.correo = 'german.colon@udea.edu.co'

print(vars(Usuario), '\n')
print(vars(usuario1))
print(vars(usuario2))'''

# Alcance encerrado: Una funcion hija puede llamar a una funcion madre(cosa que normalmente no se hace)
'''def funcion_externa():
    a = 10
    def funcion_interna():
        b = 20
        print(a, b)
    funcion_interna()
funcion_externa()'''
# Palabra reservada Nonlocal: condiciona que no se cree una variable local

def funcion_externa():
    a = 10
    def funcion_interna():
        nonlocal a
        a = 20
        print(a)
    funcion_interna()
funcion_externa()
# DIR nos devuelve una lista de nombre ordenada.
import math
espacio_nombres = dir()
if 'math' in espacio_nombres:
    print('math esta')
else:
    print('math no esta')



