# Es el proceso de comprobacion en que se verifica que los datos cumplan con los requisitos esperados.
# Es en esencia una optimizacion de los datos.

# Validacion con manejo de excepciones
'''while True:
    try:
        # Codigo a validar
        break # Finaliza la validacion.
    except [tipo de excepcion]:
        # Codigo si falla la validacion'''
# Validacion con bandera:
'''bandera = False
while not bandera:
    if [expresion de validacion]:
        bandera = True
    else:'''
# Validacion de tipo de datos:
'''while True:
    try:
        edad = int(input('Introduce tu edad: '))
        break
    except ValueError:
        print('El valor debe ser un numero entero.')
print(f'Tu edad es: {edad}.')'''

# Validacion de tipo de dato con bandera: Para comprobar si los valores de un argumento son digitos o no.
'''print('10'.isdigit())'''
'''bandera = False
while not bandera:
    edad = input('Ingresa tu edad: ')
    if edad.isdigit():
        print(f'Usted tiene {edad} años.')
        bandera = True
    else:
        print('Ingresa un numero entero.')'''
# Para mejorar la validacion se puede usar la funcion type e identificar de que tipo es el error y como solucionarlo.
'''valor = 'Python: El poder de los objetos.'
if type(valor) == str:
    print('El objeto es una cadena.')
else:
    print(f'El objeto no es una cedena :{type(valor).__name__}')'''
# Funcion predefinida isinstance():
'''valor = 'Python: El poder de los objetos.'
if isinstance(valor, str):
    print('El objeto es una cadena.')
else:
    print(f'El objeto no es una cedena :{type(valor).__name__}')'''
# Validacion de longitud
'''bandera = False
while not bandera:
    contrasena = input('Introduzca la contraseña (minimo 8 caracteres).')
    if len(contrasena) >= 8:
        bandera = True
    else:
        print('La contraseña debe tener almenos 8 caracteres.')
print(f'Contraseña establecida: {contrasena}.')'''
# Validacion de rango
bandera = False
while not bandera:
    try:
        numero = int(input('Escribe un numero del 1 al 10: '))
        if numero > 0 and numero < 11:
            bandera = True
        else:
            print('Dije un numero del 1 al 10')
    except:
        print('Eso no es un valor valido.')
print(f'El numero introducido es: {numero}.')


