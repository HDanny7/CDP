import bd.base_datos as sqlbd #importa el módulo base_datos del paquete bd y lo asigna al alias sqlbd

base_datos = sqlbd.BaseDatos(**sqlbd.acceso_bd) #crea una instancia de la clase BaseDatos y le pasa como argumentos los parámetros de conexión a la base de datos definidos en el módulo base_datos

#base_datos.mostrar_bd() #llama al método mostrar_bd de la instancia base_datos y le pasa como argumento la consulta SQL "SHOW DATABASES" para mostrar las bases de datos disponibles en el servidor MySQL

#base_datos.eliminar_bd("american_riders") #llama al método eliminar_bd de la instancia base_datos y le pasa como argumento el nombre de la base de datos "prueba" para eliminarla del servidor MySQL

base_datos.crear_bd("american_riders") #llama al método crear_bd de la instancia base_datos y le pasa como argumento el nombre de la base de datos "prueba" para crearla en el servidor MySQL
