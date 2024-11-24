# el método init es un metodo especial que podemos incluir en las clases y que no necesita ser llamado explicitamente, se llma automaticamente.
# Se puede dar un estado inicial a un objeto

'''class Usuario:
    # Atributos
    nombre = 'Sin nombre'
    apellidos = 'Sin apellidos'
    edad = 0
    direccion = 'Sin direccion'
    telefono = 'Sin telefono'

    # Métodos
    def iniciar_sesion(self):
        print('El usuario ha iniciado sesión')
    def cerrar_sesion(self):
        print('El usuario ha cerrado sesión')
    def cambiar_nombre_perfil(self):
        print('Se cambio el nombre')'''

# Atributos de clase y de instacia
# Los de clase son los que venimos haciendo, los de instancia cambian a medida que se programa
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
        print('El usuario ha iniciado sesión')
    def cerrar_sesion(self):
        print('El usuario ha cerrado sesión')
    def cambiar_nombre_perfil(self):
        print('Se cambio el nombre')

usuario1 = Usuario('Germán', 'Colón Carrasquill', 27, 'Medellín', '28827323')
print(usuario1.nombre)

# Reasignación 
usuario1.nombre = 'Ger'
usuario1.hora_ultima_sesion = ('06/11/2024')

print(usuario1.nombre)
print(usuario1.hora_ultima_sesion)


