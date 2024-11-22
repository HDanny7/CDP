# Gracias a la herencia de clases podemos crear nuevas clases que compartan caracteristicas o funciones de otras clases sin repetir codigo.
class Ciudadano:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion
    def saludar(self):
        print(f'Hola, soy {self.nombre}. Mi profesion es {self.profesion}.')
class Medico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.profesion = 'Medico'
    def sludar(self):
        print(f'Hola soy {self.nombre}. Mi profesion es {self.profesion}.')

# Clase base y clase derivada
'''Clase Base: clase principal o la que se hiso primero
Clase Derivada: Clase que hereda las caracteristicas de la clase base.'''
# Funcion predefinida super(). se hace poniendo unos () en la clase derivada.
class Qf(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, 'Químico Farmacéutico')
class Policia(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, 'Policía')

pers1 = Ciudadano('Ana', 'Informatica')
pers2 = Medico('Gabriel')
pers3 = Qf('Ger')
pers4 = Policia('Daniel')

pers1.saludar()
pers2.sludar()
pers3.saludar()
pers4.saludar()

