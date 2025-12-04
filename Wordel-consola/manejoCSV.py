import random

def leer_csv(ruta: str) -> list:
    """Lee un archivo CSV línea por línea.
    Cada línea se separa por comas y se almacena como una lista.

    Args:
        ruta (str): Ruta del archivo CSV a leer.

    Returns:
        list: Lista donde cada elemento es una fila del CSV representada como lista de strings.
    """
    datos = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            columnas = linea.split(",")
            datos.append(columnas)
    return datos


def cargar_config(ruta: str) -> dict[str, str]:
    """Carga la configuración desde un CSV y la devuelve como diccionario.
    Ignora la primera fila porque es el encabezado.

    Args:
        ruta (str): Ruta del archivo CSV.

    Returns:
        dict[str, str]: Diccionario con claves y valores de configuración.
    """
    filas = leer_csv(ruta)
    config = {}

    i = 1
    while i < len(filas):
        clave = filas[i][0]
        valor = filas[i][1]
        config[clave] = valor
        i += 1

    return config


def cargar_palabrasv2(ruta: str) -> dict:
    """Carga un CSV de palabras categorizadas y construye un diccionario donde
    cada clave es una categoría y su valor es una lista de palabras.

    Args:
        ruta (str): Ruta del archivo CSV.

    Returns:
        dict: Diccionario categoría a lista de palabras.
    """
    filas = leer_csv(ruta)

    encabezados = filas[0]

    palabras = {}
    i = 0
    while i < len(encabezados):
        categoria = encabezados[i]
        palabras[categoria] = []
        i += 1

    j = 1
    while j < len(filas):
        fila = filas[j]
        i = 0
        while i < len(encabezados):
            categoria = encabezados[i]
            palabra = fila[i]
            palabras[categoria].append(palabra)
            i += 1
        j += 1

    return palabras


def elegir_palabra_sin_repetir(palabras: dict) -> tuple:
    """Elige una palabra aleatoria de las categorías disponibles.
    Quita la palabra del diccionario para evitar repetirla.

    Args:
        palabras (dict): Diccionario categoría a palabras disponibles.

    Returns:
        tuple:(palabra, categoría) o (None, None) si no hay palabras.
    """
    palabra = None
    categoria_elegida = None
    categorias_validas = []
    
    for categoria in palabras:
        if len(palabras[categoria]) > 0:
            categorias_validas.append(categoria)

    if len(categorias_validas) == 0:
        resultado = (palabra, categoria_elegida)

    else:
        categoria_elegida = random.choice(categorias_validas)
        palabra = random.choice(palabras[categoria_elegida])
        palabras[categoria_elegida].remove(palabra)
        resultado = (palabra, categoria_elegida)

    return resultado
