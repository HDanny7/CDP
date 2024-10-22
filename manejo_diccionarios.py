# Llamar valores del diccionario
camiseta={
    "color":"rojo",
    "talla":"L",
    "precio":100,
    "unidades":10,
}
'''dato_optenido=camiseta["color"]
print(dato_optenido)

# Reasignar valores en el diccionario
camiseta["unidades"]=25
print({camiseta["unidades"]})
'''
# Crear claves y valores nuevos
camiseta["marca"]="style"
print(camiseta)
'''
# Eliminar valores o claves con palabra reservada "del"
del camiseta["color"]
print(camiseta)'''
