# Bucles con continue y anidacion
# Elementos anidados; son archivos que estan dentro de otros.
'''for expresion:
    # Bloque de codigo del bucle for
    if expresion:
        # Bucle de codigo para if'''
colores = ['rojo','azul', 'verde', 'amarillo']
#print('- LISTADO DE COLORES-')
for color in colores:
    if color == 'azul' or color ==  'verde':
        continue
    print(f'colo {color}.')
    
    
