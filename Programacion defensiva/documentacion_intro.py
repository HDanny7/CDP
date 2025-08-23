# En programacion el orden y la claridad son la maxima organizacion
# Comentarios que se hacen con una almohadilla, no deben sobrepasar 72 palabras
'''Describen el codigo, Marcan los pasos del codigo, dejar tareas, Etiquetar, Tareas pendientes, Etc.'''
# Codetags: TODO(Tarea pendiente), BUG(Error), FIXME(Funcion ineficiente, usar otra), Las etquetas se usan con el nombre de la persona que arregla el problema.
# Operador flecha(->), se usa para dar informacion implicita, sin necesidad de explicarla.
'''def longitud(cadena:str) -> int:
    return len(cadena)
print(type(longitud('Hola')))
'''
# Funcion predefinida help()
'''help(int)'''
# Con las docstring: Podras documentar elementos de tus codigos y que queden incluidos en los atributos docs de los objetos, de esa forma se crearan objetos documentados.
def par_impar(numero):
    '''
    Solicita un numero al usuario
    Esto es la docstring
    '''
    numero = int(numero)
    if numero % 2 == 0:
        print('El numero es par.')
    else:
        print('El numero es impar.')
par_impar(7)
print(par_impar.__doc__) # Llamamos el docstring donde los pusimos.


