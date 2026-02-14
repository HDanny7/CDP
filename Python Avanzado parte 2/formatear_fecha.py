#import datetime
from datetime import datetime
# Se obtiene la hora y fecha en la ejecucion
hora_actual = datetime.now()
#print(hora_actual)

# Codigo de formateo para fechas
fecha_formateada = hora_actual.strftime('%A, %d, %B, %Y')
print(fecha_formateada)



