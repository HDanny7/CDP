'''def decoradora(funcion_parametro):
    print('El resultado de la operacion es:')
    funcion_parametro()
    print('Operacion realizada con éxito.')
@decoradora
def sumar():
    print(10+10)'''

def decoradora(funcion_parametro): # La funcion_parametro es la funcion que nosotros decoramos, en este caso la suma.
    def interna():
        print('El resultado de la operacion es:')
        funcion_parametro()
        print('Operacion realizada con éxito.')
    return interna # Con este return nosotros devolvemos la funcion_parametro o lo que este contenido, sino la ponemos, esta mostrara error o no aparecera.
@decoradora # Para aplicar la decoracion a cualquier funcion es necesario el @ seguido de la funcion decoradora como tal.
def sumar():
    print(10 + 10)

sumar()



