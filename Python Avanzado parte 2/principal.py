'''import paquete.modulo1
import paquete.modulo2

paquete.modulo1.descripcion()
paquete.modulo2.descripcion()'''

# Importar un elemento de un modulo de un paquete
'''from paquete.modulo1 import suma

operacion = suma(10, 30)
print(operacion)'''

# Importar y dar alias
'''import paquete.modulo1 as md1
import paquete.modulo2 as md2

md1.descripcion()
md2.descripcion()'''

# Subpaquetes
'''import paquete.subpaquete.modulo3 as md3
import paquete.subpaquete.modulo4 as md4

md3.descripcion()
md4.descripcion()'''

# Importar paquete: Es necesario el __init__ para que se ejecuten las funciones de los modulos.

'''import paquete
paquete.modulo1.descripcion()
paquete.modulo2.descripcion()'''

# Variable especial __name__: Usado para llamar al nombre de un modulo desde otro.
# Para hacerse se debe escribir __name__ en el modulo que se quiere llamar y ejecutar en el modulo desde el que se llama.

# if __name__ == __main__:
'''import paquete'''

# Importaciones de paquetes con *: Para hacerlo de esta forma se necesita la variable especial __all__ en el modulo __init__.

from paquete import *
modulo1.descripcion()
modulo2.descripcion()



