# Se utiliza para comprobar si un valor se encuentra dentro de una secuencia.
# Utiliza dos valores: 1(el que se va a comprobar) y 2(la secuencia en la que se buscara.)

# Las posiciones de los string, cada caracter tiene una posicion en valor numerico
'''cadena = "Hola, mundo!"
lista_caracteres = list(cadena)
print(lista_caracteres)'''

# Operador In como buscador
'''texto = "La programacion es el arte de crear algo de l anada"
buscar = "arte" in texto
print(buscar)'''
# In en listas
'''colores = ["rojo", "verde", "azul", "amarillo"]
buscar = "verde" in colores'''

colores = ["rojo", "verde", "azul", "amarillo"]
print("---LISTA DE COLORES---")
for color in colores:
    print(f"-{color}")
'''if buscar:
    print("Valor encontrado")
else:
    print("Valor no encontrado")'''