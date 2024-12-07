# Argumentos posicionales: Se relacionan de forma posicional con la declaracion de parametro.
'''def suma(a, b):
    return a + b
resultado = suma(10, 30)
print(resultado)

# Argumentos de clave: Son los que se especifican como pares de clave y valor.
def suma(a, b):
    return a + b
resultado = suma(a=10, b=30)
print(resultado)

# Argumentos por defecto: Son valores que se asignan los parametros de una funcion de una forma predeterminada.
def suma(a, b=30):
    return a + b
resultado = suma(a=10)
print(resultado)'''

# Argumentos arbitrarios posicionales *ARGS: Podremos crear funciones para obtener muchos argumentos posicionales como queramos.
'''def crea_lista(*args):
    #Creamos una lista vacia.
    lista = []
    #Añadimos los datos a la lista.
    for i in args:
        lista.append(i)
    return lista

#Llamamos a la funcion
llamada = crea_lista(7, 45, 32, 134, 563, 23)
#Imprimimos la lista.
print('Los valores en la lista son', llamada)'''

'''def funcion (*args):
    print(args)
    print(type(args))

funcion(10, 20)'''
# Lo q importa es el * en args, ya que este es una convencion.
'''def funcion(*objetos):
    print(objetos)
funcion('Hola', 34.5, 19, True)'''

# ARGS es siempre el ultimo parametro
def funcion(a, b, *args):
    print(a, b, args)
funcion(1, 4, 5, 23, 45)


