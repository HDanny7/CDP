# Set son como listas con elementos inmutables, no pueden cambiar, pero se pueden agregar o eliminar pero no modificar.
# nombre_set={elemento1, elemento2,elemento3,...}
# Las listas no se pueden guardar en un set, las tuplas si se pueden guardar en set.
#lista_colores=["rojo","verde", "azul","amarillo"]
#set_colores={"rojo","verde", "azul","amarillo",[lista_colores]}
#print(set_colores) # Aparece error
tupla_colores=("rojo","verde", "azul","amarillo")
set_colores={"rojo","verde", "azul","amarillo",tupla_colores}
print(set_colores) # aparece la tupla en el set.
#set_colores={"rojo","verde", "azul","amarillo"}

#set_colores.add("marrón")
#set_colores.remove("azul")
#set_colores.discard("fucsia") # Para eliminar igual que remove, pero no aparece error si se elimina un valor que de por si no existia.

#print(set_colores)
