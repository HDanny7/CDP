import mysql.connector

# Conexión a la base de datos
acceso_bd = {"host": "localhost",
             "user": "root",
             "password": "danielcc97@",
             }

class BaseDatos:
    def __init__(self, **kwargs): #kwargs es un diccionario con los parámetros de conexión a la base de datos
        self.conector = mysql.connector.connect(**kwargs) #**kwargs es un diccionario con los parámetros de conexión a la base de datos, se pasan como argumentos a la función connect
        self.cursor = self.conector.cursor() #cursor es un objeto que permite ejecutar consultas SQL y obtener resultados


    def consulta(self, sql): #sql es una cadena con la consulta SQL a ejecutar
        self.cursor.execute(sql) #execute es un método del cursor que ejecuta la consulta SQL pasada como argumento
        return self.cursor #devuelve el cursor con los resultados de la consulta SQL ejecutada
    
    def mostrar_bd(self): #sql es una cadena con la consulta SQL a ejecutar
        self.cursor.execute("SHOW DATABASES") #execute es un método del cursor que ejecuta la consulta SQL pasada como argumento
        for bd in self.cursor: #itera sobre los resultados del cursor, que es un iterable con las filas devueltas por la consulta SQL
            print(bd) #imprime cada fila devuelta por la consulta SQL, que es una tupla con los valores de cada columna de la fila
    def eliminar_bd(self, nombre_bd): #nombre_bd es una cadena con el nombre de la base de datos a eliminar
        try:
            self.cursor.execute(f"DROP DATABASE {nombre_bd}") #execute es un método del cursor que ejecuta la consulta SQL pasada como argumento, en este caso se utiliza una f-string para insertar el nombre de la base de datos a eliminar en la consulta SQL
            print(f"Base de datos {nombre_bd} eliminada") #imprime un mensaje indicando que la base de datos ha sido eliminada, utilizando una f-string para insertar el nombre de la base de datos eliminada en el mensaje
            print("Estas son las bases de datos disponibles:") #imprime un mensaje indicando que se mostrarán las bases de datos disponibles
            self.mostrar_bd() #llama al método mostrar_bd para mostrar las bases de datos
        except:
            print(f"Error al eliminar la base de datos {nombre_bd}: puede que no exista o que esté en uso") #imprime un mensaje indicando que ha ocurrido un error al eliminar la base de datos, utilizando una f-string para insertar el nombre de la base de datos que se intentó eliminar en el mensaje
            print("Estas son las bases de datos disponibles:") #imprime un mensaje indicando que se mostrarán las bases de datos disponibles
            self.mostrar_bd() #llama al método mostrar_bd para mostrar las bases de datos

    def crear_bd(self, nombre_bd): #nombre_bd es una cadena con el nombre de la base de datos a crear
        try:
            self.cursor.execute(f"CREATE DATABASE {nombre_bd}") #execute es un método del cursor que ejecuta la consulta SQL pasada como argumento, en este caso se utiliza una f-string para insertar el nombre de la base de datos a crear en la consulta SQL
            print(f"Base de datos {nombre_bd} creada") #imprime un mensaje indicando que la base de datos ha sido creada, utilizando una f-string para insertar el nombre de la base de datos creada en el mensaje
            print("Estas son las bases de datos disponibles:") #imprime un mensaje indicando que se mostrarán las bases de datos disponibles
            self.mostrar_bd() #llama al método mostrar_bd para mostrar las bases de datos
        except:
            print(f"Error al crear la base de datos {nombre_bd}: puede que ya exista o que el nombre no sea válido") #imprime un mensaje indicando que ha ocurrido un error al crear la base de datos, utilizando una f-string para insertar el nombre de la base de datos que se intentó crear en el mensaje
            print("Estas son las bases de datos disponibles:") #imprime un mensaje indicando que se mostrarán las bases de datos disponibles
            self.mostrar_bd() #llama al método mostrar_bd para mostrar las bases de datos






