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
    def saludar(self):
        print('Tirate al suelo basura!')
# Se crean elementos con una misma identidad
policia1 = Policia('Raquel')
policia1.saludar()
medico1 = Medico('Miguel')
medico1.saludar()
