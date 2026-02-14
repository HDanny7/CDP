# El encapsulamiento es el concepto de agrupar atributos y metodos en un mismo conjunto.
#Modificadores de acceso: restringen el acceso de los atributos y metodos de las clases. Haciendo que ciertos detalles de l aimplementacion del codigo queden ocultos al usuario.
'''class Usuario:
    def __init__(self, id, nombre, apellido):
        self.id = id #Publico
        self._nombre = nombre #Protegido
        self.__apellido = apellido #Privado
    def muestra_apellido(self):
        print(self.__apellido)
# Miembros publico 
class Usuario:
    id = 1
# Acceder al atributo publico
Usuario.id = 1000
# Instanciamos un objeto
usuario_1 = Usuario()
# Comprobamos el valor de id
print(usuario_1.id)
usuario_1 = Usuario(1, 'Enrique', ' Ateortua')
print(usuario_1._nombre)

#Interfaz publica: Codigo para que todos lo puedan usar
#Publico y no publico: Codigo para uso comun o privado.

#Metodo publico para acceso privado:
usuario_1 = Usuario(1, 'Enrique', ' Marquez')
usuario_1.muestra_apellido()

# Name mangling: Modificacion de nombres de variables o metodo para evitar conflicto con nombres q se le ponga al codigo.
usuario_1 = Usuario(1, 'Ger', 'Col')
print(usuario_1._Usuario__apellido)'''

# Metodos getter y setters: Obtener y establecer
class Usuario:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.__edad = edad
    # Getter
    def obtener_edad(self):
        return self.__edad
    
    # Setter
    def establecer_edad(self, edad):
        self.__edad = edad
usurrio_1 = Usuario(1, 'Ger', 27)
'''# Almacenamos el valor de retorno
edad_usuario = usurrio_1.obtener_edad()
print(edad_usuario)'''
# Establecer edad
usurrio_1.establecer_edad(28)




