'''Herencia simple o unica, multiple, multinivel,
jerarquica e hibrida.'''
# Class object: Clase raiz predefinida de python q hereda a todas las demas clases q creamos.
# Herencia simple o unica: Proviene de una unica superclase
class A(object):
    pass

class B(A):
    pass
#Herencia multiple: una superclase recibe herencia de mas de una clase
'''class A(object):
    pass

class B(object):
    pass
class C(A, B):
    pass'''
# Herencia multinivel: Hereda una detras de la otra
'''class A(object):
    pass

class B(A):
    pass
class C(B):
    pass
class D(C):
    pass

# MRO: Orden de resolucion de metodos: Pone en una lista un camino con el recorrido de herencias que se hace.
print(D.mro())'''

# Herencia jerarquica: Cuando hay mas de una subclase de una superclase
'''class A(object):
    pass
class B(A):
    pass
class C(A):
    pass
class D(A):
    pass'''
#Herencia hibrida: Se mezclan varios tipos de herencias en una misma estructura de clase.


