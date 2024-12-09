# Iterar un iterable con posiciones simples
'''colores = ('rojo', 'azul', 'verde', 'amarillo')
for color in colores:
    print(colores)'''

# Iterar un iterable con elementos iterables dentro
'''datos = (('manzana', 'rojo'),('pera', 'verde'),('platano', 'amarillo'))
for fruto, color in datos:
    prin(f'{fruta} - {color}')'''

# Iteracion con multiples iteradores
datos1 = (('manzana', 'rojo', 'podrida'),
          ('pera', 'verde', 'madura'),
          ('platano', 'amarillo', 'verde'))
for fruto, color, estado in datos1:
    print(f'{fruto} - {color} - {estado}')


