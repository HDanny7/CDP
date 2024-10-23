# Indice de posicion: Pone numeros en las posiciones de ciertos elementos.

# Lista
colores=["azul","verde","rojo"] # Cada color tiene un numero de posicion que no vemos con el azul como 0, verde 1 y rojo 2

# Sintaxis de asignacion en listas.
colores[0]="amarillo"

print(colores)

# Error por numero de indice inesistente

colores[7]="amarillo"

# Metodos:Append, crea una nueva posicion en la lista

colores.append("amarillo")

# Metodos: insert: igual que append pero en una posicion especifica

colores.insert(0,"amarillo")

# Metodos: extend:extiendde una lista con un elemento iterable

colores=["azul","verde","rojo"]
colores2=["amarillo","naranja","marron"]
colores.extend(colores2)
print(colores)
