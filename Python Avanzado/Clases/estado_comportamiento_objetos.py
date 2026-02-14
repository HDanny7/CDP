# Los objetos pueden tener estado y comportamiento(Atributos y metodos)

class Jugador():
    # Atributo de clase
    edad = None
    
    # Metodo
    def permitir_acceso(self):
        print('Puede entrar')
    def denegar_acceso(self):
        print('Acceso denegado')
    def comprobar_edad(self):
        if self.edad < 18:
            self.denegar_acceso()
        else:
            self.permitir_acceso()
# Objeto creado a partir de la clase
jugador1 = Jugador()
jugador2 = Jugador()

# Llamado al metodo
jugador1.edad = 15
jugador2.edad = 60

jugador1.comprobar_edad()
jugador2.comprobar_edad()
# Identidad de los objeto: Podemos referirnos a ellos de forma inequivoca por esta identidad.


