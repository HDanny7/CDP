# Metodo index: nombre_listas,index(elemento)
numeros=[38,34,83,87,23,45,12,98,40,75,87,23,45,12,98,40,75]
buscar_numero=numeros.index(40)
print(buscar_numero) # Busca el valor en la posicion, 40 esta en la posicion 8

# Metodo count: busca todas la coincidencias de la lista
valor_busqueda=int(input("Introduzcar valor a buscar\n"))
coincidencias=numeros.count(valor_busqueda)
print(coincidencias)