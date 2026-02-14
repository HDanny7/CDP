#Se pueden Crear estados y comportamientos a los objetos con diferencias.

class Ciudadano:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion
    def saludar(self):
        print(f'Hola, soy {self.nombre}. Mi profesion es {self.profesion}.')
class Medico(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, 'Médico')
    def curar(self):
        print('Cura cualquier daño')

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
pers2.curar()
pers3.saludar()
pers4.saludar()

