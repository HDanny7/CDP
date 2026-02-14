# Bucle while true y do while: Python no lo tiene, pero se puede emular.
numero = int(input('Introduzca un numero: '))

while True: # Bucle infinito
    print(f'El numero es {numero}.')
    numero += 1 # Se incrementa en 1
    
    if numero == 7777: # Se busca detener el bucle cuando llegue a este valor
        print('El conteo termino.')
        break # Rompe el bucle cuando este cumpla la condicion IF

