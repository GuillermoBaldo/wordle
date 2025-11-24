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


def escribir_csv(ruta: str, filas: list) -> None:
    """Sobrescribe por completo un archivo CSV.

    Args:
        ruta (str): Ruta del archivo CSV a escribir.
        filas (list): Contenido que se escribirá, cada fila como lista de strings.

    Returns:
        None
    """
    with open(ruta, "w", encoding="utf-8") as archivo:
        for fila in filas:
            linea = ",".join(fila)
            archivo.write(linea + "\n")


def agregar_fila(ruta: str, fila: list) -> None:
    """Agrega una fila al final del archivo CSV.

    Args:
        ruta (str): Ruta del archivo CSV.
        fila (list): Fila a agregar, en forma de lista de strings.

    Returns:
        None
    """
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(",".join(fila) + "\n")


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


def editar_config(ruta: str, clave: str, nuevo_valor: str) -> None:
    """Edita un valor dentro del archivo config.csv.

    Args:
        ruta (str): Ruta del archivo CSV.
        clave (str): Clave a modificar.
        nuevo_valor (str): Valor que reemplazará al anterior.

    Returns:
        None
    """
    filas = leer_csv(ruta)

    i = 1
    while i < len(filas):
        if filas[i][0] == clave:
            filas[i][1] = nuevo_valor
            break
        i += 1

    escribir_csv(ruta, filas)


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


def cargar_palabras(ruta: str) -> dict:
    """Carga un archivo palabras.csv con formato categoría-palabra
    y devuelve un diccionario agrupado por categorías.

    Args:
        ruta (str): Ruta del archivo CSV.

    Returns:
        dict: Diccionario con categorías y sus palabras asociadas.
    """
    filas = leer_csv(ruta)
    palabras = {}

    i = 1
    while i < len(filas):
        categoria = filas[i][0]
        palabra = filas[i][1]

        if categoria not in palabras:
            palabras[categoria] = []

        palabras[categoria].append(palabra)
        i += 1

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
