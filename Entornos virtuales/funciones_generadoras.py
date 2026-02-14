# Funciones generadoras: Permiten dividir una ejecucion de funcion en partes mas pequeñas. Forman un objeto iterador que se ejecuta paso a paso.
# Palabra reservada YIELD
'''def generadora():
    for i in range(0, 100):
        print(i)
print(generadora())'''

'''def generadora_numeros():
    lista_valores = []
    for i in range(0, 100):
        lista_valores.append(i)
    return lista_valores
valores = generadora_numeros()
print(valores)'''

'''def generadora():
    for i in range(0, 100):
        yield i # Vas pausando y ejecutando una funcion
rango = generadora()
print(next(rango))
print(next(rango)) 
print(next(rango)) # etc. Para funciones que manejen muchos valores, podemos dividir las llamadas.'''

'''def generadora():
    for i in range(0, 10):
        if i % 2 == 0:
            yield f'{i} - par'
        else:
            yield f'{i} - impar'
rango = generadora()
print(next(rango))
print(next(rango)) 
print(next(rango))'''
# Objeto iterador: Crean elementos sobre la marcha y no se guardan en la memoria, ejecutan a medida que se van usando.
# Objetos iterables: Es cualquier objeto que se pueda iterar mediante un bucle.

'''cadena = 'Hola'
cadena_generadora = iter(cadena)
print(type(cadena_generadora))
print(next(cadena_generadora))
print(next(cadena_generadora))
print(next(cadena_generadora))
print(next(cadena_generadora))'''

def generadora():
    for i in range(0, 10):
        if i % 2 == 0:
            yield f'{i} - par'
        else:
            yield f'{i} - impar'
rango = generadora()
lista_generadora = list(rango)
print(lista_generadora[7])
print(lista_generadora[2])
