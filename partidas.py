from funciones_espesificas import *
from manejoCSV import *
from mostrar_datos import * 
from comodines import *
import random

def configurar_partida(estado_partida: dict, palabras: list[str]):
    """Inicializa una nueva partida seleccionando palabra, tema y 
    reiniciando contadores e indicadores.

    Args:
        estado_partida (dict): Estado del juego.
        palabras (list[str]): Lista de palabras para elegir.
    """

    palabras_elegidas = elegir_palabra_sin_repetir(palabras)
    estado_partida["tema"] = palabras_elegidas[1]
    estado_partida["secreto"] = normalizar_palabra(palabras_elegidas[0])

    print(estado_partida["secreto"])
    estado_partida["intentos"] = 1
    estado_partida["comodines_usados"] = 0
    estado_partida["ganaste"] = False
    estado_partida["bandera_comodines"] = [True, True, True]

def jugar(estado_partida: dict, palabras: list[str], config) -> None:
    """Controla el flujo general del juego: configura, ejecuta la partida
    y muestra la palabra si el jugador pierde.

    Args:
        estado_partida (dict): Estado actual de la partida.
        palabras (list[str]): Lista de palabras disponibles.
    """

    configurar_partida(estado_partida, palabras) 
    jugar_partida(estado_partida, config)
    if not estado_partida["ganaste"]:
        print(f'Se acabaron los intentos. La palabra era: {config["RED"]}{estado_partida["secreto"]}{config["RESET"]}\n')

def jugar_partida(estado_partida: dict, config) -> bool:
    """Ejecuta una partida completa: solicita palabras, valida, muestra feedback
    y determina si el jugador ganó.

    Args:
        estado_partida (dict): Estado actual de la partida.

    Returns:
        bool: True si el jugador ganó, False si perdió.
    """
    while estado_partida["intentos"] <= int(config["MAX_ATTEMPTS"]):
        palabra = intentos_partida(estado_partida, config)
        palabra_validada = validar_adivinanza(palabra)
        if not palabra_validada:
            print("Entrada inválida. Introduce exactamente 5 letras.")
            continue
        
        sistema_comodines(palabra_validada, estado_partida, config)

        validar_palabra(palabra_validada, estado_partida, config)
        if estado_partida["ganaste"]:
            break

    return estado_partida["ganaste"]

def intentos_partida(estado_partida: dict, config) -> str:
    """Solicita al jugador que ingrese una palabra para el intento actual.

    Args:
        estado_partida (dict): Contiene información de la partida (nivel, intentos, vidas, puntaje y la palabra secreta).
        config (_type_): Configuración general del juego

    Returns:
        str: La palabra ingresada por el jugador ya normalizada.
    """
    print(f'Nivel {estado_partida["nivel"]} | Partida {estado_partida["partida"]} | Vidas {estado_partida["vidas"]} | Puntos {estado_partida["puntaje"]}')
    palabra = input(f'Intento {estado_partida["intentos"]}/{config["MAX_ATTEMPTS"]}: ')
    palabra = normalizar_palabra(palabra)
    return palabra

def validar_palabra(palabra_validada: str, estado_partida: dict, config: dict) -> None:
    """Valida la palabra ingresada por el jugador y actualiza el estado de la partida.
        - Muestra freedback si la palabra no es AYUDA.
        - Marca la partida como ganada si coincide con la palabra secreta.
        - Si no coincide (y no es AYUDA), incrementa intentos y errores.

    Args:
        palabra_validada (str): Palabra ya normalizada ingresada por el jugador.
        estado_partida (dict): Contiene datos como la palabra secreta, intentos, errores, vidas y puntaje.
        config (dict): Configuración del juego (colores y parámetros globales).
    
    Returns:
        None
    """
    if palabra_validada != "AYUDA":
        mostrar_feedback(palabra_validada, estado_partida["secreto"], config)
        
    if palabra_validada == estado_partida["secreto"]:
        print(f'¡Felicidades! Adivinaste la palabra en {config["GREEN"]}{estado_partida["intentos"]}{config["RESET"]} intentos.\n')
        estado_partida["ganaste"] = True
    
    elif palabra_validada != estado_partida["secreto"] and palabra_validada != "AYUDA":
        estado_partida["intentos"] += 1
        estado_partida["errores"] += 1
