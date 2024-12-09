# Metodo Items()
'''argumentos = {'Nombre': 'Enrique',
              'Edad': 27,
              'Telefono': 8748238}
print(type(argumentos.items()))
print(argumentos.items())'''

# Una forma de unir KWARGS con las bibliotecas e iterar sus datos.
def info(**kwargs):
    for clave, valor in kwargs.items():
        print(f'Clave: {clave}, Valor: {valor}')
argumentos = {'Nombre': 'Enrique',
              'Edad': 27,
              'Telefono': 8748238}
info(**argumentos)



