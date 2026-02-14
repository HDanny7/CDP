'''# Te permiten confirmar si algunas condiciones especificas son ciertas en ciertas partes del codigo.
a = 1
assert a == 0, 'El valor no es cero'
'''
'''numeros = [1, 2, 3, 4 ,5 ,6]
assert 7 in numeros, 'No se encuentra'
'''
'''numeros = [1, 2, 3, 4 ,5 ,6]
assert 7 not in numeros, 'No se encuentra'
'''
'''numeros = [1, 2, 3, 4 ,5 ,6]
assert isinstance (numeros, tuple), 'El objeto no es una tupla'
'''
'''numeros = [1, 2, 3, 4 ,5 ,6]
assert isinstance (numeros, list), 'El objeto es una no lista'
'''
'''import imc

try:
    peso = float(input('Ingrese su peso en kg \n'))
    altura = float(input('Ingrese su altura en mmetros \n'))

    indice_masa_corporal = imc.calcular_imc(peso, altura)
    print(f'Su indice de masa corporal (IMC) es: {round(indice_masa_corporal,2)}')

except ValueError:
    print('Error: Ingrese valores validos en las categorias peso y altura')
'''



