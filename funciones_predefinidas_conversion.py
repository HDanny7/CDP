'''numero1=input("Introducir primer numero")
numero2=input("Introducir segundo numero")
print(type(numero1))
print(type(numero2))
'''
# El proble es que el input es para string, lo que aparece es una concatenacion de los valores mas no una suma

# Se soluciona el problema definiendo los valores de numero1 y numero2
'''numero1=input("Introducir primer numero")
numero2=input("Introducir segundo numero")
numero1=int(numero1)
numero2=int(numero2)
print(numero1+numero2)
'''
# Mejorado
numero1=int(input("Introducir primer numero"))
numero2=int(input("Introducir segundo numero"))
print(numero1+numero2)