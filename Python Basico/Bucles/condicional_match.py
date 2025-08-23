# Permite escribir muchas condiciones pero de forma simple.
codigo = input("Introduzca un codigo HTTP:")
match codigo:
    case "200":
        print("Todo OK")
    case "301":
        print("Movimiento permanente de la pagina")
    case "302":
        print("Movimiento temporarl de la pagina")
    case "404":
        print("Pagina no encontrada")
    case "500":
        print("Error interno del servidor")
    case "503":
        print("Servicio no disponible")
    case _:
        print("Codigo no disponible")



