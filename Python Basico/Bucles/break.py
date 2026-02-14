# Bucles con break; Descarta iteraciones.

colores = ['rojo','azul', 'verde', 'amarillo']
#print('- LISTADO DE COLORES-')
for color in colores:
    if color == 'azul':
        break
        continue
    print(f'-color {color}' )