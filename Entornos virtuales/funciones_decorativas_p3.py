def a(b):
    def c(num1, num2):
        print('El resultado de la operacion es:')
        b(num1, num2)
        print('Operacion realizada con éxito.')
    return c

@a    
def sumar(num1, num2):
    print(num1 + num2)

sumar(40, 54)
sumar(100, 305)
sumar(48, 52)






