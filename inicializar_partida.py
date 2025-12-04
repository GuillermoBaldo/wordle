import pygame
from recursos_juego.boton import * 
from manejoCSV import *

def crear_letras_objetivo(palabra):
    """Convierte la palabra secreta en una lista de letras individuales.

    Args:
        palabra (str): Palabra completa.

    Returns:
        list: Lista con cada letra por separado.
    """
    letras = []
    i = 0
    while i < len(palabra):
        letras.append(palabra[i])
        i += 1
    return letras

def crear_matriz_vacia(filas, columnas, valor):
    """Crea una matriz (lista de listas) con un valor inicial repetido.

    Args:
        filas (int): Cantidad de filas.
        columnas (int): Cantidad de columnas.
        valor: Valor inicial para cada posición.

    Returns:
        list: Matriz generada con el valor dado.
    """
    matriz = []
    f = 0
    while f < filas:
        fila = []
        c = 0
        while c < columnas:
            fila.append(valor)
            c += 1
        matriz.append(fila)
        f += 1
    return matriz

def crear_botones_partida(ventana):
    """Crea los tres botones usados durante la partida 
    (revelar letra, revelar categoría y comodín extra).

    Args:
        ventana: Ventana de pygame donde se dibujan los botones.

    Returns:
        dict: Diccionario con los botones creados.
    """
    boton_revelar_letra = crear_boton(ventana, (140, 45), (20, 535), texto="Revelar letra")
    boton_revelar_cat = crear_boton(ventana, (140, 45), (175, 535), texto="Revelar tema")
    boton_extra = crear_boton(ventana, (160, 45), (335, 535), texto="Letra sin orden")
    
    botones = (boton_revelar_letra,boton_revelar_cat, boton_extra)

    return botones

def crear_fuentes(config):
    """Crea las fuentes principales que se usarán en la partida.

    Args:
        config (dict): Configuración general que contiene las fuentes.

    Returns:
        dict: Diccionario con las fuentes creadas.
    """
    fuente_tit = pygame.font.SysFont(*config["FUENTES"]["TITULO"])
    fuente_sub = pygame.font.SysFont(*config["FUENTES"]["SUBTITULO"])

    fuentes = {
        "fuente_tit": fuente_tit,
        "fuente_sub": fuente_sub
    }

    return fuentes

def construir_estado_partida(palabra, categoria, letras_obj, intentos, colores, fuentes, botones, config, puntos_actuales, datos_imagen):
    """Construye el diccionario que guarda todo el estado de la partida,
    incluyendo palabra, intentos, colores, botones, fuentes y puntaje.

    Args:
        palabra (str): Palabra secreta.
        categoria (str): Categoría de la palabra.
        letras_obj (list): Letras objetivo.
        intentos (list): Matriz de intentos ingresados por el jugador.
        colores (list): Matriz de colores para cada letra.
        fuentes (dict): Fuentes para texto.
        botones (dict): Botones de la partida.
        config (dict): Configuración general.
        puntos_actuales (int): Puntos del usuario.

    Returns:
        dict: Estado completo de la partida.
    """
    
    estado = {
        "palabra": palabra,
        "categoria": categoria,
        "letras_obj": letras_obj,
        "intentos": intentos,
        "colores": colores,
        "fuente_tit": fuentes["fuente_tit"],
        "fuente_sub": fuentes["fuente_sub"],
        "colores_grilla": config["COLORES"],
        "reloj": pygame.time.Clock(),

        "tema_revelado": False,
        "pos_letra": 0,
        "intento_actual": 0,

        "resultado": "",
        "terminar": False,

        "puntos": puntos_actuales,
        "errores_totales": 0,

        "botones": botones,

        "img_corazon": cargar_imagen_corazon("imagenes/Corazon.png", (30, 30)),
        "datos_imagen":datos_imagen
    }
    return estado

def cargar_imagen_corazon(path, size):
    """Carga y escala la imagen del corazón para mostrar vidas/puntos.

    Args:
        path (str): Ruta de la imagen.
        size (tuple): Tamaño final (ancho, alto).

    Returns:
        Surface: Imagen cargada y escalada
    """
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, size)
    return img

def inicializar_partida(ventana, config, palabras, datos):
    """Inicializa una nueva partida: elige una palabra, crea matrices,
    botones, fuentes y arma el estado del juego.

    También contempla el caso en que ya no quedan palabras disponibles.

    Args:
        ventana: Ventana principal del juego.
        config (dict): Configuraciones generales.
        palabras (list): Lista de palabras disponibles.
        datos (dict): Información del usuario (puntos, etc.).

    Returns:
        dict: Estado inicial de la partida.
    """

    palabra_secreta, categoria = elegir_palabra_sin_repetir(palabras)
    print(palabra_secreta, categoria)

    estado = {}

    # Caso extremo: no quedan palabras
    if palabra_secreta is None:
        estado = {
            "terminar": True,
            "resultado": "perdio",
            "puntos": datos["puntos_totales"],
            "errores_totales": 0,
            "comdin_usado1": False, 
            "comdin_usado2": False
        }
    else:
        palabra_secreta = palabra_secreta.upper()

        letras_obj = crear_letras_objetivo(palabra_secreta)
        intentos = crear_matriz_vacia(6, 5, "")
        colores = crear_matriz_vacia(6, 5, "blanco")
        fuentes = crear_fuentes(config)
        botones = crear_botones_partida(ventana)
        imagen = pygame.transform.scale(pygame.image.load("imagenes/colores.webp.png").convert_alpha(), (70, 70))
        rect_imagen = imagen.get_rect(topleft=(0, 55)) 
        datos_imagen = (imagen, rect_imagen)
        # Construye el estado interno de la partida usando puntos actuales del diccionario
        estado = construir_estado_partida(
            palabra_secreta,
            categoria,
            letras_obj,
            intentos,
            colores,
            fuentes,
            botones,
            config,
            datos["puntos_totales"],
            datos_imagen 
        )

    return estado

