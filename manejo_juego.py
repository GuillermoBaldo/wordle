from mostrar_datos import *
from manejoJSON import *
from manejoCSV import *
import time

def manejo_niveles(estado_partida: dict) -> None:
    """Actualiza el nivel y la partida según si el jugador ganó.

    Args:
        estado_partida (dict): Estado actual de la partida.

    Returns:
        None
    """
    if estado_partida["ganaste"]:
        if estado_partida["partida"] == 3:
            estado_partida["nivel"] +=1 
            estado_partida["partida"] =0
        estado_partida["partida"] +=1
    
def manejo_puntaje_x_comodines (estado_partida: dict, puntos_x_comodin: int) -> None:
    """Descuenta puntos según la cantidad de comodines usados.

    Args:
        estado_partida (dict): Estado actual de la partida.
        puntos_x_comodin (int): Puntos a restar por cada comodín usado.

    Returns:
        None
    """
    match estado_partida["comodines_usados"]:
        case 1:
            estado_partida["puntaje_ronda"] -= puntos_x_comodin
        case 2:
            estado_partida["puntaje_ronda"] -= puntos_x_comodin * 2
        case 3:
            estado_partida["puntaje_ronda"] -= puntos_x_comodin * 3

def manejo_puntaje_x_intentos (estado_partida: dict, puntos_x_intento: int) -> None:
    """Suma puntos según la cantidad de intentos usados para adivinar la palabra.

    Args:
        estado_partida (dict): Estado de la partida.
        puntos_x_intento (int): Puntos base por intento.

    Returns:
        None
    """
    match estado_partida["intentos"]:
        case 1:
            estado_partida["puntaje_ronda"] += puntos_x_intento * 6
        case 2:
            estado_partida["puntaje_ronda"] += puntos_x_intento * 5
        case 3:
            estado_partida["puntaje_ronda"] += puntos_x_intento * 4
        case 4:
            estado_partida["puntaje_ronda"] += puntos_x_intento * 3
        case 5:
            estado_partida["puntaje_ronda"] += puntos_x_intento * 2
        case 6:
            estado_partida["puntaje_ronda"] += puntos_x_intento * 1

def manejo_puntaje_derrota(estado_partida: dict, puntos_x_perdida: int, config) -> None:
    """Descuenta puntos si el jugador no adivinó la palabra.

    Args:
        estado_partida (dict): Estado de la partida.
        puntos_x_perdida (int): Puntos que se restan al perder.

    Returns:
        None
    """
    if not estado_partida["ganaste"]:
        print(f"se te descontaran {puntos_x_perdida} puntos por no haber adivinado la palabra")
        estado_partida["puntaje_ronda"] -= puntos_x_perdida
    
def manejo_puntaje(estado_partida: dict, config , puntos_x_comodin: int = 20, puntos_x_intento: int = 50 , puntos_x_perdida: int = 100 ) -> None:
    """Calcula el puntaje final de una partida aplicando reglas de intentos, comodines y derrota.

    Args:
        estado_partida (dict): Estado de la partida.
        puntos_x_comodin (int, optional): Descuento por comodín. Default 20.
        puntos_x_intento (int, optional): Puntos por intento. Default 50.
        puntos_x_perdida (int, optional): Descuento por perder. Default 100.

    Returns:
        None
    """
    estado_partida["puntaje_ronda"] = 0
    
    manejo_puntaje_x_comodines(estado_partida, puntos_x_comodin)
    manejo_puntaje_x_intentos(estado_partida, puntos_x_intento)
    manejo_puntaje_derrota(estado_partida, puntos_x_perdida ,config)
    color = config["GREEN"]
    
    if estado_partida["puntaje_ronda"] < 0:
        color = config["RED"]
    
    print(f"puntos ganados en la partida: {color}{estado_partida["puntaje_ronda"]}{config["RESET"]}\n")
    estado_partida["puntaje"] += estado_partida["puntaje_ronda"]

def manejo_vidas(estado_partida: dict) -> int:
    """Actualiza las vidas restantes según si el jugador ganó o perdió la ronda.

    Args:
        estado_partida (dict): Estado de la partida.

    Returns:
        int: Cantidad actualizada de vidas.
    """
    if not estado_partida["ganaste"]:
        estado_partida["vidas"] -= 1
    return estado_partida["vidas"]


