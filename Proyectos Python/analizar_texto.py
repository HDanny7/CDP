# Crear una funcion que analiza texto
def analizar_texto(texto):
    # Convertir todo el texto en minuscula para uniformidad
    texto = texto.lower()
    
    # Separamaos palabras asumiendo que a estas las separa un espacio
    palabras = texto.split()

    # Crear un diccionario para contar la cantidad de palabras en el texto
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    # Encontrar la palabra mas comun
    palabra_comun = max(frecuencia, key=frecuencia.get)

    # Analiixar sentimientos simples dependiendo de algunas palabras claves
    palabras_positivas = ['genial', 'bueno', 'excelente', 'feliz', 'maravilloso']
    palabras_negativas = ['malo', 'terrible', 'horrible', 'triste', 'desagradable']

    puntaje_sentimiento = 0
    for palabra in palabras:
        if palabra in palabras_positivas:
            puntaje_sentimiento += 1
        elif palabra in palabras_negativas:
            puntaje_sentimiento -= 1
    
    sentimiento = ''
    if puntaje_sentimiento > 0:
        sentimiento = 'positivo'
    elif puntaje_sentimiento < 0:
        sentimiento = 'negativo'
    else:
        sentimiento = 'neutral'
    
    # Retornar resultados
    return {
        'total_palabras': len(palabras),
        'palabra_comun': palabra_comun,
        'frecuencia': frecuencia,
        'sentimiento': sentimiento
    }

# Ejecucion de ejemplo
def main():
    # Solicitamos el texto a analizar
    texto_usuario = input('Introduzca texto para analizar: ')
    
    resultados = analizar_texto(texto_usuario)

    print('\n--- Resultados del Análisis ---')
    print(f'Total de palabras: {resultados['total_palabras']}')
    print(f'Palabra mas común: {resultados['palabra_comun']}')
    print(f'Sentimiento estimado: {resultados['sentimiento']}')
    print('\nFrecuencia de cada palabra:')
    for palabra, conteo in resultados['frecuencia'].items():
        print(f'{palabra}: {conteo}')

if __name__ == '__main__':
    main()
















