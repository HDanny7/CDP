'''Debe estar siempre en la primera posicion de cada metodo y atributo que se crea.
Sirve para representar a los objetos, sirven para llamar a los metodos y atributos de un objeto.
Self simplifica la sintaxis para llamar un objeto.'''

# Utlizar atributos en los metodos de clase
class Usuario:
    hora_ultima_sesion = None
    def __init__(self, 
                 nombre, 
                 apellidos, 
                 edad, 
                 direccion, 
                 telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
    
    def iniciar_sesion(self):
        print(f'El usuario {self.nombre} ha iniciado sesión')
    def cerrar_sesion(self):
        print('El usuario ha cerrado sesión')
    def cambiar_nombre_perfil(self):
        print('Se cambio el nombre')

usuario1 = Usuario('Germán', 'Colón Carrasquill', 27, 'Medellín', '28827323')
usuario1.iniciar_sesion()

# Reasignación 
'''usuario1.nombre = 'Ger'
usuario1.hora_ultima_sesion = ('06/11/2024')

print(usuario1.nombre)
print(usuario1.hora_ultima_sesion)'''


