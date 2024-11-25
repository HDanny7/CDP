# Se usa para ocultar los detalles complejos e irrelevantes de los codigos.
# busca facilitar el entendimiento de los conceptos.
'''Clases abstractas: Son clase diseñadas para ser utilizadas solo por la subclase por medio de la herencia.
No se pueden crear objetos de esa clase pero si de sus subclases.'''
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print('Woof!')
class Gato(Animal):
    def hablar(self):
        print('Meow!')       

perro = Perro()
perro.hablar()
gato = Gato()
gato.hablar()


