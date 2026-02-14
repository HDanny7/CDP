import funciones

# Tareas
# Menu
while True:
    print('\n Tareas')
    print('1. Anadir tarea')
    print('2. Ver tareas')
    print('3. Marcar tarea como completada')
    print('4. Eliminar tarea')
    print('5. Salir')

    # Entrada de datos
    print('\n')
    opcion = input('Introduzca una opción.\n')
    # Menu de opciones

    match opcion:
        case '1':
            funciones.agregar_tarea(funciones.tareas)
        case '2':
            funciones.ver_tareas(funciones.tareas)
        case '3':
            funciones.tarea_completada(funciones.tareas)
        case '4':
            funciones.eliminar_tarea(funciones.tareas)
        case '5':
            print('El programa se esta cerrando...')
            break
        case _:
            print('Opción inválida')

