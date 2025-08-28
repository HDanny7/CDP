# Programacion dirigida a objetos.
# Clases: son un sistema de generadores de objetos. Cada uno con sus propias caracteristicas.
# Ejemplo:
'''
class Taza():
    color = 'blanco'
    mensaje = None
    material = 'porcelana'
    limpia = True

taza_1 = Taza()
taza_1.limpia = False
taza_2 = Taza()
taza_2.mensaje = 'El café esta riko'
print(taza_1)
print(taza_2)
# De esta forma se ha hecho de forma simple la implementacion de las clases.
'''
'''
# Las clases en cirto sentido tienen partes, metodos y atributos.
# Elemplo:

# Clase vehiculo
class Vehiculo():
    # Son los atributos de la clase.
    # Normalmente primero especificamos los atributos de la clase: Estas son las caracteristicas propias del objeto.
    color = None
    longitud_metros = None
    ruedas = 4

    # Metodos son aquellas funciones(acciones) del objeto en cuestion.
    def arrancar(self):
        print('El vehiculo esta en movimiento')

    def detener(self):
        print('El vehiculo se detuvo')

# Instanciamos la clase: Instanciar es aplicar la clase a un objeto.
vehiculo_1 = Vehiculo()

# Llamamos al metodo
vehiculo_1.arrancar()
vehiculo_1.detener()

# tambien se puede definir un atributo propio de un objeto por fuera de la clse creada.
vehiculo_2 = Vehiculo()
vehiculo_2.color = 'rojo' # Le atribuimos un color a este nuevo objeto.
print(f'El color del vehiculo es {vehiculo_2.color}')
'''
# Metodo constructor: Es un metodo especial que se ejecuta al momento de instanciar la clase.
# Se define con el nombre __init__
# Los usamaos para inicializar los atributos del objeto. osea darle un valor inicial.
# Ejemplo:
class Vehiculo():
    # Estos son llamados atributos de clase de instancia.
    def __init__(self, color, longitud_metros, ruedas): # El metodo constructor recibe parametros.
        self.color = color # El self hace referencia al objeto que se esta creando.
        self.longitud_metros = longitud_metros
        self.ruedas = ruedas

    def arrancar(self):
        print('El vehiculo esta en movimiento')

    def detener(self):
        print('El vehiculo se detuvo')

vehiculo_1 = Vehiculo('rojo', 4.5, 4) # Al instanciar la clase le pasamos los argumentos que pide el constructor. Estos se escriben en el mismo orden.
print(f'El color del vehiculo es {vehiculo_1.color}, tiene una longitud de {vehiculo_1.longitud_metros} metros y tiene {vehiculo_1.ruedas} ruedas.')

# Self: Es una referencia al objeto que se esta creando. Siempre debe ser el primer parametro de los metodos de la clase.
# Permite acceder a los atributos y metodos del objeto dentro de la clase.

