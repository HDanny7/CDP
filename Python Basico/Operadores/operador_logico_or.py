# Compara dos expresiones pero menos estricto que el operador and.
a = 15
b = 17
c = 13

comparacion1 = a < b or b > c
comparacion2 = a > b or b < c
print(comparacion1)
print(comparacion2)