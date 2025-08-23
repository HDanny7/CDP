# Defenderse de las escepciones
# TRY: Se utiliza para ejecutar un bloque de codigo.
'''try: # Es como pedirle al interprete que haga algo aqui en try, y si no puede que haga lo que esta en except.
    pass
except:
    pass
finally: # Siempre sujeto a un bloque try y opcionalmente a un bloque except.
    pass'''

def dividir(dividiendo, divisor):
    try: 
        resultado = round(dividiendo / divisor, 2)
        print(resultado)
    except ZeroDivisionError: # Se puede hacer sin especificar el tipo de error. Esto no es recomendado ya que nos espcificas que tipo de solucion dar a diferentes tipos de errores.
        print('No se puede dividir por cero')
    finally:
        print('La operacion ha terminado.')
dividir(10, 0)









