# ============================================
#  FUNCIONES BASE PARA MANEJO DE ARCHIVOS CSV
#  (SIN USAR EL MÓDULO csv Y SIN LIST COMPS)
# ============================================

def leer_csv(ruta):
    """
    Lee un archivo CSV línea por línea.
    Cada línea se separa por comas y se guarda en una lista.
    Devuelve: lista de listas.
    """
    datos = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            columnas = linea.split(",")
            datos.append(columnas)
    return datos


def escribir_csv(ruta, filas):
    """
    Sobrescribe completamente un CSV.
    'filas' debe ser una lista de listas.
    """
    with open(ruta, "w", encoding="utf-8") as archivo:
        for fila in filas:
            linea = ",".join(fila)
            archivo.write(linea + "\n")


def agregar_fila(ruta, fila):
    """
    Agrega una sola fila al final del archivo CSV.
    'fila' debe ser una lista con strings.
    """
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(",".join(fila) + "\n")


# ============================
#  CARGAR CONFIGURACIÓN
# ============================

def cargar_config(ruta):
    """
    Convierte config.csv en un diccionario:
    clave → valor.

    Saltea la primera fila porque es el encabezado.
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


def editar_config(ruta, clave, nuevo_valor):
    """
    Modifica un valor en config.csv.
    Busca la clave y reemplaza el valor.
    """
    filas = leer_csv(ruta)

    i = 1  # empieza después del encabezado
    while i < len(filas):
        if filas[i][0] == clave:
            filas[i][1] = nuevo_valor
            break
        i += 1

    escribir_csv(ruta, filas)


# ============================
#  ESTADO DEL JUGADOR
# ============================

def cargar_estado_jugador(ruta):
    """
    Carga un estado de jugador tipo:
    {
        "partida": "1",
        "nivel": "1",
        "vidas": "3",
        ...
    }
    """
    filas = leer_csv(ruta)

    encabezados = filas[0]
    valores = filas[1]

    estado = {}
    i = 0
    while i < len(encabezados):
        clave = encabezados[i]
        valor = valores[i]
        estado[clave] = valor
        i += 1

    return estado


def guardar_estado_jugador(ruta, estado):
    """
    Guarda el estado del jugador en el CSV.
    Respeta el orden de los encabezados.
    """
    filas = leer_csv(ruta)
    encabezados = filas[0]

    nueva_fila = []

    i = 0
    while i < len(encabezados):
        clave = encabezados[i]
        nueva_fila.append(str(estado[clave]))
        i += 1

    filas[1] = nueva_fila  # reemplazar fila de datos

    escribir_csv(ruta, filas)


# ============================
#  MANEJO DE PALABRAS
# ============================

def cargar_palabras(ruta):
    """
    Convierte palabras.csv en:
    {
        "animales": ["gato","perro"],
        "colores": ["rojo","azul"],
        ...
    }
    """
    filas = leer_csv(ruta)
    palabras = {}

    i = 1  # saltar encabezado
    while i < len(filas):
        categoria = filas[i][0]
        palabra = filas[i][1]

        if categoria not in palabras:
            palabras[categoria] = []

        palabras[categoria].append(palabra)
        i += 1

    return palabras


# ============================
#  ELEGIR PALABRA SIN REPETIR
# ============================

import random

import random

def elegir_palabra_sin_repetir(palabras):
    """
    Devuelve (palabra, categoria) al azar.
    Quita la palabra elegida del diccionario.
    SOLO 1 return.
    """

    palabra = None
    categoria_elegida = None

    # Construir lista de categorías que tengan palabras
    categorias_validas = []
    for categoria in palabras:
        if len(palabras[categoria]) > 0:
            categorias_validas.append(categoria)

    # Si NO hay categorías válidas → devuelve (None, None)
    if len(categorias_validas) == 0:
        resultado = (palabra, categoria_elegida)

    else:
        # Elegimos una categoría al azar
        categoria_elegida = random.choice(categorias_validas)

        # Elegimos una palabra al azar dentro de esa categoría
        palabra = random.choice(palabras[categoria_elegida])

        # La removemos para no repetirla nunca más
        palabras[categoria_elegida].remove(palabra)

        resultado = (palabra, categoria_elegida)

    # ÚNICO RETURN DE TODA LA FUNCIÓN
    return resultado
