# Lista de tareas
tareas = []

# Funciones del programa
def agregar_tarea(lista):
    # Entrada para la tarea
    tarea = input('Introduzca la descripcion de la tarea:\n')
    # Añadir tarea al final de la lista
    lista.append(tarea)

    # Informe de tarea añadida
    print('\nLa tarea se añadio a la lista de tareas pendientes.\n')

    # Imprime la tarea añadida
    print(f'La tarea añadida es : {tarea}.')

    # Informe del numero de tarea
    print(f'La tarea se almaceno en la posición {len(lista)}\n')


def ver_tareas(lista):
    # Condicional que evalua si algo esta en la lista de tareas
    
    # Si hay algo en la lista, se presenta
    if lista:
        for indice, tarea in enumerate(lista):
            print(f'{indice + 1}. {tarea}. ')

    # Si la lista esta vacia, avisa de ellos
    else:
        print('No hay tareas pendientes')

    #Mensaje de fin de listado
    print('--Fin del listado--')
def tarea_completada(lista):
    # Llamamos a la funcion ver_tarea()
    ver_tareas(lista)
    if not lista:
         print('Para marcar tarea completada debe añadir una tarea.')
    else:
        # Entrada para que el usuario introduzca una tarea
        completada = int(input('Introduzca el numero de la tarea a marcar como completada:\n'))

        # Condiciones para marcar tareas como completadas
        if completada > 0 and completada <= len(lista):

            # Condicional para evaluar si la tarea ya esta completada
            # Si ya la tarea esta completada...
            if '(completada)' in lista[completada - 1]: 
                    print('La tarea ya esta completada.')

            else:
                    lista[completada - 1] = '(completada)' + lista[completada - 1]
                    print('Se marco la tarea como completada.')
            # En cambio, si no esta...
        else:
                print('Opcion invalida')
# Avisar si la opcion elegida es invalida

def eliminar_tarea(lista):

    # Si la lista contiene algo:
    if lista:
        # llamamos a la funcion ver_tareas()
        ver_tareas(lista)
        # Entrada para que elusuario introduzca una tarea
        tarea = int(input('Introduzca el numero de la tarea.\n'))
        # Opcion invalida si l atarea no esta en el rango de la lista
        if tarea <= 0 or tarea > len(lista):
            print('Opcion invalida.')
        # Si la opcion es valida se elimina la tarea
        else:
            del lista[tarea - 1]
            print('Se elimino la tarea.')
        # Si la lista esta vacia se avisa de ello
    else:
        print('No hay tareas.')
