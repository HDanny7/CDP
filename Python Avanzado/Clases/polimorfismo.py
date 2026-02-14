# Capacidad de un objeto para tener varias formas.
# Len: Es una de las palabras reservadas que tiene varias funciones dependiendo del contexto.
'''class Animal:
    def hablar(self):
        print('Soy un animal.')
class Perro(Animal):
    def hablar(self):
        print('Wooof!!.')
class Gato(Animal):
    def hablar(self):
        print('Meow!!.')
animal = Animal()
perro = Perro()
gato = Gato()

animal.hablar()
perro.hablar()
gato.hablar()

#Polimorfismo con funciones
def dar_voz(objeto):
    objeto.hablar()
dar_voz(animal)
dar_voz(perro)
dar_voz(gato)'''
'''
#Sobrecarga y sobreescritura: Uno agrega mas variacion y el otro mas informacion

#Funcion con 4 parametros
def multiplicacion(a, b, c, d):
    print(a*b*c*d)
multiplicacion(10, 2, 3, 6)
 #Funcion con 2 paremetros
def multiplicacion(a, b):
    print(a * b)
multiplicacion(5, 7,)'''

def multiplicacion(a, b, c=None, d=None):
    if c is not None:
        if d is not None:
            print(a * b * c * d)
        else:
            print(a * b * c)
    else:
        print(a * b)
multiplicacion(10, 3, 10, 2)
            




