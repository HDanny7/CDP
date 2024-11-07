# Se llama instanciar a un objeto cuando este es creado por una clase; Instanciar es la accion de crear objetos(Instancia=objeto)

class Vehiculo():
    # Atributos
    color = None # None quiere decir que no tiene valor la variable
    longitud = None
    ruedas = 4

    # Metodos
    def arrancar(self):
        print('El motor ha arrancado')
    def detener(self):
        print('El motor esta detenido')

# Instanciamos dos objetos de tipo vehiculo
objeto_vehiculo_1 = Vehiculo()
objeto_vehiculo_2 = Vehiculo()

# Acceder al atributo de un objeto

print(objeto_vehiculo_1.ruedas)

# Almacenar el atributo en una variable
ruedas_vehiculo = objeto_vehiculo_1.ruedas

# Reasignar los valores a los atributos de objetos

objeto_vehiculo_1.color = 'Negro'
objeto_vehiculo_2.color = 'Rojo'

print(objeto_vehiculo_1.color)
print(objeto_vehiculo_2.color)

# Crear atributos inexistentes en la clase

objeto_vehiculo_1.velocidad_maxima = 160

print(objeto_vehiculo_1.velocidad_maxima)


# Problemas por atributos externos a la clase

# Llamar a un metodo de un objeto

objeto_vehiculo_1.arrancar()



