# Solicitar la longitud del lado
lado = float(input('Ingresa la longitud del lado:\n')) # En cm para este y todos los datos.

# Calcular el area
A = lado * lado

# Mostrar el resultado
print(f'El area del cuadrado es: {A} cm.')

# Calcular el perimero del cuadrado(Suma de cada uno de los laos del cuadrado)

P = lado + lado + lado + lado

print(f'El perimetro del cuadrado es: {P} cm.')

# Convertir el ejercicio en funcion
def A_cuadrado():
    # Solicitar la longitud del lado
    lado = float(input('Ingresa la longitud del lado:\n')) # En cm para este y todos los datos.

    # Calcular el area
    A = lado * lado

    # Mostrar el resultado
    print(f'El area del cuadrado es: {A} cm.')

    # Calcular el perimero del cuadrado(Suma de cada uno de los laos del cuadrado)

    P = lado + lado + lado + lado

    print(f'El perimetro del cuadrado es: {P} cm.')
A_cuadrado()