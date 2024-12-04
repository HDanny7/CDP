import locale
import datetime

# Establecer el idioma en español
locale.setlocale(locale.LC_ALL, 'es')
# Se obtiene la hora y fecha en la ejecucion
hora_actual = datetime.datetime.now()
#print(hora_actual)

# Codigo de formateo para fechas
fecha_formateada = hora_actual.strftime('%A, %d, %B, %Y')
print(fecha_formateada)



