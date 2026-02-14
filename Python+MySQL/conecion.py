import mysql.connector

# Establecer la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="danielcc97",
    database = 'prueba' # Asegúrate de que esta base de datos exista antes de ejecutar el código
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()
'''
# Mostrar las bases de datos existentes
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)

# Crear una nueva base de datos
try:
    cursor.execute("CREATE DATABASE prueba;") # Si tratas de ejecutar esto más de una vez, te dará error porque ya existe la base de datos
    print("Base de datos creada")
except:
    print("Aparecio un error al crear la base de datos")

# Eliminar una base de datos
try:
    cursor.execute("DROP DATABASE prueba;") # Si tratas de ejecutar esto más de una vez, te dará error porque ya no existe la base de datos
    print("Base de datos eliminada")
except:
    print("Aparecio un error al eliminar la base de datos")
'''
# Crear una tabla
try:    
    cursor.execute("""
        CREATE TABLE clientes (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            apellido VARCHAR(100) NOT NULL,
            telefono VARCHAR(15) NOT NULL,
            direccion VARCHAR(255)
        );
    """)
    print("Tabla creada")
except:
    print("Aparecio un error al crear la tabla")



