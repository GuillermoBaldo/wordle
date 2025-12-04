import random
import pygame

def obtener_color_celda(estado_celda: str, config) -> tuple[int, int, int]:
    """Devuelve el color RGB según el estado de la celda."""
    
    if config["DALTONISMO"]:
        colores = {
            "verde": (config["COLORES"]["VERDE"]),
            "amarillo": (config["COLORES"]["AMARILLO"]),
            "gris_claro": (config["COLORES"]["GRIS_CLARO"]),
            "blanco": (config["COLORES"]["BG"])
        }
    else:
        colores = {
            "verde": (config["COLORES"]["AZUL"]),
            "amarillo": (config["COLORES"]["NARANJA"]),
            "gris_claro": (config["COLORES"]["GRIS_CLARO"]),
            "blanco": (config["COLORES"]["BG"])
        }
    return colores.get(estado_celda, colores["blanco"])


def dibujar_celda(ventana, rect, color_fondo):
    """Dibuja una celda con borde."""
    pygame.draw.rect(ventana, color_fondo, rect, border_radius=8)
    pygame.draw.rect(ventana, (179, 0, 134), rect, 3, border_radius=10)


def dibujar_letra_en_celda(ventana, rect, letra, fuente, color_texto):
    """Dibuja la letra centrada en la celda."""
    imagen_letra = fuente.render(letra, True, color_texto)
    ventana.blit(
        imagen_letra,
        (
            rect.centerx - imagen_letra.get_width() // 2,
            rect.centery - imagen_letra.get_height() // 2
        )
    )


def dibujar_grilla(ventana: pygame.Surface, config: dict, estado: dict) -> None:
    """Dibuja la grilla de 6 filas x 5 columnas."""
    TAM_CELDA = 65
    ESPACIO = 10
    FILAS = 6
    COLUMNAS = 5
    Y_INICIO = 80

    ancho_total = COLUMNAS * TAM_CELDA + (COLUMNAS - 1) * ESPACIO
    x_inicio = config["ANCHO"] // 2 - ancho_total // 2

    f = 0
    while f < FILAS:
        c = 0
        while c < COLUMNAS:

            estado_celda = estado["colores"][f][c]
            color_fondo = obtener_color_celda(estado_celda, config)

            rect = pygame.Rect(
                x_inicio + c * (TAM_CELDA + ESPACIO),
                Y_INICIO + f * (TAM_CELDA + ESPACIO),
                TAM_CELDA, TAM_CELDA
            )

            dibujar_celda(ventana, rect, color_fondo)

            letra = estado["intentos"][f][c]
            if letra != "":
                dibujar_letra_en_celda(
                    ventana,
                    rect,
                    letra,
                    estado["fuente_tit"],
                    estado["colores_grilla"]["NEGRO"]
                )

            c += 1
        f += 1


def letra_aparece_en_palabra(letra: str, palabra_obj: list) -> bool:
    """
    Verifica manualmente si una letra aparece dentro de la palabra objetivo.
    - No usa "in"
    - No usa while anidado
    - Solo 1 return

    Args:
        letra (str): Letra a buscar.
        palabra_obj (list): Letras de la palabra objetivo.

    Returns:
        bool: True si aparece, False si no.
    """
    aparece = False
    j = 0
    while j < len(palabra_obj):
        if palabra_obj[j] == letra:
            aparece = True
        j += 1

    return aparece


def asignar_color_letra(estado: dict, indice: int) -> None:
    """
    Asigna color a una letra según su coincidencia con la palabra objetivo.
    (verde, amarillo, gris_claro)
    - No usa while anidado.
    - Usa una función auxiliar para verificar si la letra aparece en la palabra.

    Args:
        estado (dict): Estado actual del juego.
        indice (int): Posición de la letra en el intento actual.

    Returns:
        None
    """
    intento = estado["intentos"][estado["intento_actual"]]
    palabra_obj = estado["letras_obj"]
    letra = intento[indice]
    letra_obj = palabra_obj[indice]

    colores_fila = estado["colores"][estado["intento_actual"]]

    if letra == letra_obj:
        colores_fila[indice] = "verde"
    else:
        aparece = letra_aparece_en_palabra(letra, palabra_obj)

        if aparece:
            colores_fila[indice] = "amarillo"
        else:
            colores_fila[indice] = "gris_claro"


def colorear_intento(estado: dict) -> None:
    """
    Colorea todas las letras del intento actual según su acierto:
    verde, amarillo o gris_claro.
    - Evita while anidado dividiendo la lógica en funciones.
    - Mantiene exactamente el comportamiento original.

    Args:
        estado (dict): Diccionario del juego.

    Returns:
        None
    """
    i = 0
    while i < 5:
        asignar_color_letra(estado, i)
        i += 1



def obtener_indices_vacios(intento):
    """Devuelve una lista con las posiciones del intento que aún están vacías.

    Recorre las 5 posiciones del intento y agrega a la lista todos los índices
    cuyo valor sea una cadena vacía "" (es decir, donde todavía no se colocó letra).

    Args:
        intento (list): Lista de tamaño 5 con letras o cadenas vacías.

    Returns:
        list: Índices donde el intento todavía no tiene letra.
    """
    indices = []
    i = 0
    while i < 5:
        if intento[i] == "":
            indices.append(i)
        i += 1
    return indices


def obtener_posiciones_no_verdes(colores):
    """Devuelve los índices donde el color NO es verde.

    Se utiliza para determinar qué posiciones aún no fueron acertadas 
    correctamente. Si una posición no es verde, sigue siendo candidata
    para revelar información (amarillos o verdes automáticos).

    Args:
        colores (list): Lista de colores para cada posición del intento.

    Returns:
        list: Índices cuyo color es distinto de "verde".
    """
    posiciones = []
    i = 0
    while i < 5:
        if colores[i] != "verde":
            posiciones.append(i)
        i += 1
    return posiciones


def posibles_indices_amarillos(indices_vacios, indice_real):
    """Calcula qué posiciones vacías pueden usarse para colocar una letra amarilla.

    Excluye la posición real de la letra correcta, ya que colocarla ahí sería
    un acierto verde, no un amarillo.

    Parámetros:
        indices_vacios (list): Índices aún no ocupados en el intento.
        indice_real (int): Posición de la letra dentro de la palabra objetivo.

    Retorna:
        list: Índices vacíos válidos para colocar una letra amarilla.
    """
    posibles = []
    i = 0
    while i < len(indices_vacios):
        if indices_vacios[i] != indice_real:
            posibles.append(indices_vacios[i])
        i += 1
    return posibles



def revelar_verde(intento, palabra_obj, colores, indices_vacios):
    """Revela una letra correcta en su posición exacta (color verde).

    Selecciona aleatoriamente una posición vacía dentro del intento,
    toma la letra correspondiente de la palabra objetivo y la coloca
    en esa posición marcándola como 'verde'.

    Args:
        intento (list): Lista del intento actual.
        palabra_obj (str): Palabra que debe adivinarse.
        colores (list): Lista de colores para cada posición.
        indices_vacios (list): Índices donde no hay letras colocadas.

    Returns:
        str: La letra revelada en verde.
    """
    indice = random.choice(indices_vacios)
    letra = palabra_obj[indice]

    intento[indice] = letra
    colores[indice] = "verde"

    return letra


def revelar_amarillo(intento, palabra_obj, colores, indices_vacios):
    """Revela una letra amarilla en el intento actual.

    Este helper busca una posición de la palabra objetivo que aún no esté marcada
    como verde (posición correcta), toma aleatoriamente una de ellas y luego busca 
    un lugar vacío del intento donde colocarla como amarilla, siempre que:
        - No coincida con la posición real (para no marcarla verde).
        - No coincida con otra letra igual en esa misma posición.

    Args:
        intento (list): Lista con las letras del intento actual, incluyendo espacios vacíos.
        palabra_obj (str): La palabra objetivo que el jugador debe adivinar.
        colores (list): Lista de colores ("verde", "gris", "amarillo") para cada posición.
        indices_vacios (list): Índices donde el intento aún no tiene letra asignada.

    Returns:
        str o None: La letra revelada como amarilla, o None si no se pudo colocar.
    """
    resultado = None

    posiciones_no_verdes = obtener_posiciones_no_verdes(colores)

    if posiciones_no_verdes:
        indice_real = random.choice(posiciones_no_verdes)
        letra = palabra_obj[indice_real]

        posibles_amarillos = []
        for idx in indices_vacios:
            if idx != indice_real and palabra_obj[idx] != letra:
                posibles_amarillos.append(idx)

        if posibles_amarillos:
            indice_colocado = random.choice(posibles_amarillos)
            intento[indice_colocado] = letra
            colores[indice_colocado] = "amarillo"
            resultado = letra

    return resultado



def revelar_letra_grilla(estado: dict, permitir_ubicacion_incorrecta: bool = False) -> str | None:
    """
    Revela una letra en la grilla como comodín.
    - Verde = posición correcta
    - Amarillo = posición incorrecta
    """
    intento_actual = estado["intento_actual"]
    palabra_obj = estado["letras_obj"]
    intento = estado["intentos"][intento_actual]
    colores = estado["colores"][intento_actual]

    resultado = None
    indices_vacios = obtener_indices_vacios(intento)

    if indices_vacios:
        if not permitir_ubicacion_incorrecta:
            resultado = revelar_verde(intento, palabra_obj, colores, indices_vacios)
        else:
            resultado = revelar_amarillo(intento, palabra_obj, colores, indices_vacios)

    estado["letra_revelada"] = resultado
    return resultado


def verificar_ganador(estado: dict) -> bool:
    """Verifica si el intento actual coincide exactamente con la palabra a adivinar.

    Args:
        estado (dict): Estado del juego.

    Returns:
        bool: True si ganó, False si perdió.
    """
    intento = estado["intentos"][estado["intento_actual"]]
    objetivo = estado["letras_obj"]

    ganador = True
    i = 0

    while i < 5:
        if intento[i] != objetivo[i]:
            ganador = False
        i += 1

    return ganador
