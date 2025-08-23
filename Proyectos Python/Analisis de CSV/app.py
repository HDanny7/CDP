import os
import csv
import statistics
import matplotlib.pyplot as plt

# Definimos una ruta para la carga de nuestros archivos
def cargar_datos_csv(ruta_archivo):
    
    try:
        # Verificar que el archivo existe
        if not os.path.exists(ruta_archivo):
            print(f"Error: El archivo '{ruta_archivo}' no existe")
            return None, None
        # Leer el archivo CSV
        encabezados = []
        datos = []

        with open(ruta_archivo, 'r', newline='', encoding='latin-1') as archivo_csv:
            # Crear un lector CSV
            lector = csv.reader(archivo_csv)
            # Leer la primera linea como encabezados
            encabezados = next(lector)

            # Leer los datos
            for fila in lector:
                # Crear un diccionario para cada fila
                if len(fila) == len(encabezados):
                    fila_dict = {}
                    for i, valor in enumerate(fila):
                        try:
                            # Primero intentarr convertir a entero
                            fila_dict[encabezados[i]] = int(valor)
                        except ValueError:
                        
                            try:
                                # Si no es entero, intentar convertir a float
                                fila_dict[encabezados[i]] = float(valor)
                            except ValueError:
                                # Si no es numero, dejar como string
                                fila_dict[encabezados[i]] = valor
                    datos.append(fila_dict)
        print(f'Se cargaron {len(datos)} filas de datos con {len(encabezados)} columnas.')
        return encabezados, datos
    except Exception as e:
        print(f'Error al cargar el archivo CSV: {e}')
        return None, None

def mostrar_resumen_datos(encabezados, datos):
    if not datos:
        print('No hay datos para mostrar.')
        return
    
    print('\n=== RESUMEN DE DATOS ===')
    print(f'Total de registros: {len(datos)}')
    print(f'Columnas: {', '.join(encabezados)}')

    # Mostrar las primeras 5 filas
    print('\nPrimeras 5 filas:')
    for i, fila in enumerate(datos[:5]):
        print(f'fila {i+1}: {fila}')


def analizar_columna_numerica(datos, columna):
    '''
    Realizar un analisis estadistico de una columna numerica
    Args:
        datos: Lista de diccionarios con los datos
        columna: Nombre de la columna a analizar
    Returns:
        dict: Diccionario con las estadisticas de la columna'''

    # Extraer los valores de la columna, filtrando solo los numericos.
    valores = []
    for fila in datos:
        if columna in fila and isinstance(fila[columna], (int, float)):
            valores.append(fila[columna])

    # Verificar que hay valores numericos
    if not valores:
        print(f"No se encontraron valores numericos en la columna '{columna}'.")
        return None

    # Calcular estadisticas
    estadisticas = {
        'columna': columna,
        'total_valores': len(valores),
        'minimo': min(valores),
        'maximo': max(valores),
        'suma': sum(valores),
        'promedio': sum(valores) / len(valores),
        'mediana': statistics.median(valores),
        'desviacion_estandar': statistics.stdev(valores) if len(valores) > 1 else 0
    }
    return estadisticas

def mostrar_estadisticas(estadisticas):
    '''
    Muestra las estadisticas de una columna
    Args:
        estadisticas: Diccionario con estadistica de la columna
    '''
    if not estadisticas:
        return
    
    print(f"\n=== ESTADISTICAS DE LA COLUMNA '{estadisticas['columna']}' ===")
    print(f'Total de valores: {estadisticas['total_valores']}')
    print(f'Valor minimo: {estadisticas['minimo']}')
    print(f'Valor maximo: {estadisticas['maximo']}')
    print(f'Suma: {estadisticas['suma']}')
    print(f'Promedio: {estadisticas['promedio']:.2f}')
    print(f'Mediana: {estadisticas['mediana']:.2f}')
    print(f'Desviacion estandar: {estadisticas['desviacion_estandar']:.2f}')

def generar_grafico_barras(datos, columna_x, columna_y, titulo=None):
    '''
    Generar un grafico de barras mostrando el promedio de los calores de Y para cada valor de X
    Args:
        datos: Lista de diccionarios con los datos
        columna_x: Nombre de la columna para el eje X
        columna_y: Nombre de la columna para el eje Y
        titulo: Titulo del grafico (Opcional)
    Returns:
        bool: True si se genero el grafico correctamente, False en caso contrario
        '''
    try:
        # Agrupar datos por valores de X y calcular promedios de Y
        grupos_x = {}

        for fila in datos:
            if columna_x in fila and columna_y in fila and isinstance(fila[columna_y], (int, float)):
                valor_x = str(fila[columna_x])
                valor_y = fila[columna_y]

                if valor_x not in grupos_x:
                    grupos_x[valor_x] = []
                
                grupos_x[valor_x].append(valor_y)
        # Calcular promedios para cada grupo
        valores_x = []
        promedios_y = []

        for valor_x, valores_y in grupos_x.items():
            if valores_y: # Verificar que hay valores
                valores_x.append(valor_x)
                promedios_y.append(sum(valores_y) / len(valores_y))
        
        # verificar que hay datos suficientes
        if len(valores_x) < 2:
            print('No hay sufiicientes datos para generar el grafico.')
            return False
        
        # Crear el grafico
        plt.figure(figsize=(10, 6))
        plt.bar(valores_x, promedios_y, color= 'skyblue')

        # Añadir etiquetas y titulo
        plt.xlabel(columna_x)
        plt.ylabel(f'Promedio de {columna_y}')
        plt.title(titulo or f'Promedio de {columna_y} por {columna_x}')

        # Rotar etiquetas del eje X si son muchas
        if len(valor_x) > 5:
            plt.xticks(rotation=45, ha='right')

        # Ajustar layout
        plt.tight_layout()

        # Mostrar el grafico
        plt.show()

        return True
    except Exception as e:
        print(f'Error al generar el grafico: {e}')
        return False

def generar_grafico_lineas(datos, columna_x, columna_y, titulo=None):
    '''
    Generar un grafico de lineas mostrando el promedio de los calores de Y para cada valor de X
    Args:
        datos: Lista de diccionarios con los datos
        columna_x: Nombre de la columna para el eje X
        columna_y: Nombre de la columna para el eje Y
        titulo: Titulo del grafico (Opcional)
    Returns:
        bool: True si se genero el grafico correctamente, False en caso contrario
        '''
    try:
            # Agrupar datos por valores de X y calcular promedios de Y
        grupos_x = {}

        for fila in datos:
            if columna_x in fila and columna_y in fila and isinstance(fila[columna_y], (int, float)):
                valor_x = str(fila[columna_x])
                valor_y = fila[columna_y]

            if valor_x not in grupos_x:
                grupos_x[valor_x] = []
                
            grupos_x[valor_x].append(valor_y)
        
        # Calcular promedios para cada grupo
        valores_x = []
        promedios_y = []

        for valor_x, valores_y in grupos_x.items():
            if valores_y: # Verificar que hay valores
                valores_x.append(valor_x)
                promedios_y.append(sum(valores_y) / len(valores_y))

        # verificar que hay datos suficientes
        if len(valores_x) < 2:
            print('No hay sufiicientes datos para generar el grafico.')
            return False
        
        # Crear el grafico
        plt.figure(figsize=(10, 6))
        plt.plot(valores_x, promedios_y, marker= 'o', linestyle= '-', color= 'green')

        # Añadir etiquetas y titulo
        plt.xlabel(columna_x)
        plt.ylabel(f'Promedio de {columna_y}')
        plt.title(titulo or f'Tendencia del promedio de {columna_y} por {columna_x}')

        # Rotar etiquetas del eje X si son muchas
        if len(valor_x) > 5:
            plt.xticks(rotation=45, ha='right')

        # Ajustar layout
        plt.tight_layout()

        # Mostrar el grafico
        plt.show()


        return True
    except Exception as e:
        print(f'Error al generar el grafico: {e}')
        return False

# Funcion principal del programa
def main():
    print('=== ANALIZADOR DE DATOS ===')

    # Solicitar la ruta del archivo CSV
    ruta_archivo= input('Ingrese la ruta del archivo CSV a analizar: ')

    # Cargar los datos
    encabezados, datos = cargar_datos_csv(ruta_archivo)

    if not datos:
        print('No se pudieron cargar los datos. Finalizando programa.')
        return
    
    # Mostrar resumen de los datos
    mostrar_resumen_datos(encabezados, datos)

    while True:
        # Menu de opciones
        print('\nOpciones:')
        print('1. Analizar una columna numerica')
        print('2. Generar grafico de barras')
        print('3. Generar grafico de linea')
        print('4. Salir')

        opcion = input('\nSelecciona una opcion (1-4): ')

        if opcion == '1':
            # Analizar una columna numerica
            print('\nColumna disponibles:')
            for i, columna in enumerate(encabezados, 1):
                print(f'{i}.{columna}')
            
            indice_columna = int(input('\nSelecciona el numero de la columna a analizar: ')) - 1

            if 0 <= indice_columna < len(encabezados):
                columna = encabezados[indice_columna]
                estadistica = analizar_columna_numerica(datos, columna)
                if estadistica:
                    mostrar_estadisticas(estadistica)
            else:
                print('Seleccion no valida.')
        
        elif opcion == '2':
            # Generar grafico de barras
            print('\nSelecciona las columnas para el grafico de barras:')

            print('\nColumns para el eje X:')
            for i, columna in enumerate(encabezados, 1):
                print(f'{i}. {columna}')

            indice_x = int(input('\nSelecciona el numero de la columna para el eje X: ')) - 1

            print('nColumnas para el eje Y:')
            for i, columna in enumerate(encabezados, 1):
                print(f'{i}. {columna}')

            indice_y = int(input('\nSelecciona el numero de la columna para el eje Y: ')) - 1

            if 0 <= indice_x < len(encabezados) and 0 <= indice_y < len(encabezados):
                columna_x = encabezados[indice_x]
                columna_y = encabezados[indice_y]
                titulo = input('\nIngresa un titulo para el grafico (opcional): ')

                generar_grafico_barras(datos, columna_x, columna_y, titulo)
            else:
                print('Seleccion no valida.')

        elif opcion == '3':
            # Generar grafico de lineas
            print('\nSelecciona las columnas para el grafico de lineas:')

            print('\nColumns para el eje X:')
            for i, columna in enumerate(encabezados, 1):
                print(f'{i}. {columna}')

            indice_x = int(input('\nSelecciona el numero de la columna para el eje X: ')) - 1

            print('nColumnas para el eje Y:')
            for i, columna in enumerate(encabezados, 1):
                print(f'{i}. {columna}')

            indice_y = int(input('\nSelecciona el numero de la columna para el eje Y: ')) - 1

            if 0 <= indice_x < len(encabezados) and 0 <= indice_y < len(encabezados):
                columna_x = encabezados[indice_x]
                columna_y = encabezados[indice_y]
                titulo = input('\nIngresa un titulo para el grafico (opcional): ')

                generar_grafico_lineas(datos, columna_x, columna_y, titulo)
            else:
                print('Seleccion no valida.')
        
        elif opcion == '4':
            # Salir
            print('\n¡Gracias por usar el Analiizador de Datos!')
            break
        else:
            print('Opcion no valida.')

if __name__ == '__main__':
    main()
















