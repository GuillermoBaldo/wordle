from manejoJSON import actualizar_estadisticas
from pantallas.pantalla_jugar import *

def crear_datos_juego():
    """Actualiza los datos del juego según el resultado de la partida jugada.

    Args:
        resultado (str): "perdio" o "gano".
        puntos (int): Puntos obtenidos en la partida.
        errores (int): Errores cometidos en la partida.
        datos (dict): Diccionario del estado del juego.
    """
    datos_juego= {
        "vidas": 3,
        "puntos_totales": 0,
        "errores_totales": 0,
        "nivel": 1,
        "partida": 1,
        "terminar": False,
        "tiempo": 0
    }
    return datos_juego

def procesar_resultado_partida(resultado: str, puntos: int, errores: int, datos: dict):
    """Actualiza los datos del juego según el resultado de la partida jugada.

    Args:
        resultado (str): "perdio" o "gano".
        puntos (int): Puntos obtenidos en la partida.
        errores (int): Errores cometidos en la partida.
        datos (dict): Diccionario del estado del juego.
    """
    if resultado == "perdio":
        datos["vidas"] -= 1

    datos["puntos_totales"] += puntos
    datos["errores_totales"] += errores

    if datos["vidas"] <= 0:
        datos["terminar"] = True


def ejecutar_partidas_de_nivel(VENTANA: pygame.surface, config: dict, palabras_diccionario: list, usuario: dict, datos: dict):
    """ Maneja hasta 3 partidas dentro de un mismo nivel.
        Se detiene si el jugador pierde todas las vidas.

    Args:
        VENTANA: Ventana principal de Pygame.
        config (dict): Configuraciones del juego.
        palabras_diccionario (list): Lista de palabras para jugar.
        usuario (dict): Datos del usuario actual.
        datos (dict): Estado del juego.
    """
    datos["partida"] = 1
    datos["terminar"] = False

    while datos["partida"] <= 3 and not datos["terminar"]:

        resultado, puntos, errores = pantalla_jugar(
            VENTANA,
            config,
            palabras_diccionario,
            datos
        )

        procesar_resultado_partida(resultado, puntos, errores, datos)

        print("Resultado:", resultado, "Puntos:", puntos, "Errores:", errores)
        print(usuario["nombre"])

        actualizar_estadisticas(usuario["nombre"], datos)
        if resultado != "perdio":
            datos["partida"] += 1



def jugar_niveles(palabras_diccionario: list, config: dict, VENTANA: pygame.surface, usuario: dict):
    """Controla la progresión por los niveles del juego.
        Cada nivel contiene hasta 3 partidas.

    Args:
        palabras_diccionario (list): Palabras disponibles para jugar.
        config (dict): Configuraciones del juego.
        VENTANA: Ventana principal de Pygame.
        usuario (dict): Datos del usuario actual.
    """
    datos = crear_datos_juego()

    while datos["nivel"] <= 3 and not datos["terminar"]:

        ejecutar_partidas_de_nivel(
            VENTANA,
            config,
            palabras_diccionario,
            usuario,
            datos
        )

        datos["nivel"] += 1


