# Errores de syntasis: Son los mas comunes y los mas faciles de resolver.
'''if (a > b) {}'''
# Errores de nombre: Cuando llamamos a identificadores que no existen.
'''print(variable)'''
# Errores de logica: Relacionados a los calculos matematicos y orden.
'''numero = 0
while numero < 4:
    numero += 1
    print(numero)'''
# errores semanticos: Son aquellos que aun teniendo una sintasis correcta no funcionan muy bien.
'''def sumar(a, b):
    return a + b
print(sumar('Hola', 'Mundo')) # La funcion no es para concatenar.'''
# Errores en tiempo de ejecucion: Son errores que son correctos en cuanto a logica, semantica y sintasis pero que al ejecutarse se presenta un error.
'''def dividir(a, b):
    return a / b
dividendo = int(input('Dividendo: '))
divisor = int(input('Divisor: '))
operacion = dividir(dividendo, divisor)
print(operacion) # El error se presenta cuando le pasamos un valor diferente a los que normalmente acepta, por ejemplo en ves de numero le pasamos un caracter.'''







