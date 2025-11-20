from funciones import *
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

def manejo_puntaje_derrota(estado_partida: dict, puntos_x_perdida: int) -> None:
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
    
def manejo_puntaje(estado_partida: dict, puntos_x_comodin: int = 20, puntos_x_intento: int = 50 , puntos_x_perdida: int = 100 ) -> None:
    """Calcula el puntaje final de una partida aplicando reglas de intentos, comodines y derrota.

    Args:
        estado_partida (dict): Estado de la partida.
        puntos_x_comodin (int, optional): Descuento por comodín. Default 20.
        puntos_x_intento (int, optional): Puntos por intento. Default 50.
        puntos_x_perdida (int, optional): Descuento por perder. Default 100.

    Returns:
        None
    """
    config = importar_configuracion("/Users/guille/Documents/computacion/wordle/archivos/config.csv")
    estado_partida["puntaje_ronda"] = 0
    
    manejo_puntaje_x_comodines(estado_partida, puntos_x_comodin)
    manejo_puntaje_x_intentos(estado_partida, puntos_x_intento)
    manejo_puntaje_derrota(estado_partida, puntos_x_perdida)
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

def resumen_nivel(estado_partida: dict) -> None:
    """Muestra el resumen estadístico cuando el jugador pasa de nivel.

    Args:
        estado_partida (dict): Estado de la partida.

    Returns:
        None
    """
    config = importar_configuracion("/Users/guille/Documents/computacion/wordle/archivos/config.csv")
    if estado_partida["nivel"] >1 and estado_partida["partida"] == 1:
        print(f"{config["GREEN"]}Felicidades has pasado al nivel {estado_partida["nivel"]}!{config["RESET"]}")
        print("las estadisticas de tu partida son las siguientes:")
        print(f"Puntos Totales {estado_partida["puntaje"]} | Cantidad Errores {estado_partida["errores"]} | Nivel Alcanzado {estado_partida["nivel"] -1 }")
                
def menu(usuario: dict) -> None:
    """Controla el flujo del juego, mostrando el menú y ejecutando las opciones seleccionadas.

    Args:
        usuario (dict): Datos del usuario logueado.

    Returns:
        None
    """
    inicio = time.time()
    estado_partida , palabras= inicializar_partida()
    config = importar_configuracion("/Users/guille/Documents/computacion/wordle/archivos/config.csv")
    choice = mostrar_menu() 
    while  estado_partida["vidas"] != 0 and (estado_partida["partida"] <= int(config["MAX_PARTIDAS"])) and estado_partida["nivel"] <= int(config["MAX_NIVELES"]):
        match choice:
            case "1":
                resumen_nivel(estado_partida)
                jugar(estado_partida, palabras)
                manejo_puntaje(estado_partida)
                manejo_vidas(estado_partida)
                manejo_niveles(estado_partida)
                actualizar_estadisticas(usuario["nombre"], estado_partida["puntaje_ronda"], estado_partida["errores"], estado_partida["nivel"])
            case "2":
                mostrar_instrucciones_juego()
                choice = mostrar_menu()
            case "3":
                print("Salir. ¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Intenta de nuevo.\n")
                choice = mostrar_menu()
    fin = time.time()
    finalizar_juego(estado_partida, inicio, fin)

def inicializar_partida() -> tuple[dict, list]:
    """Inicializa las variables necesarias para comenzar una partida.

    Returns:
        tuple[dict, list]: Estado inicial de la partida y lista de palabras cargadas.
    """
    estado_partida = {
    "nivel": 1,
    "partida": 1,
    "vidas": 3,
    "puntaje": 0,
    "puntaje_ronda": 0,
    "comodines_usados": 0,
    "errores": 0,
    "intentos_fallidos": 0,
    "secreto": None,
    "tema": None,
    "ganaste" : False,
	"bandera_comodines" :[True, True, True],
    "intentos": 0
    }
    palabras=cargar_palabrasv2("/Users/guille/Documents/computacion/wordle/archivos/palabras (1).csv")

    return estado_partida , palabras
    
def finalizar_juego(estado_partida: dict, inicio: float, fin: float) -> None:
    """Muestra el resultado final del juego y estadísticas completas del jugador.

    Args:
        estado_partida (dict): Estado final de la partida.
        inicio (float): Tiempo inicial del juego.
        fin (float): Tiempo final del juego.

    Returns:
        None
    """
    if estado_partida["vidas"] == 0:
        print("perdiste mal ahi")
    else:
        print("sos todo crack ganaste")
        total_segundos = fin - inicio

        minutos = total_segundos // 60     
        segundos = total_segundos % 60     

        print(f"Tiempo total: {minutos:.0f} min {segundos:.2f} seg")
        print(f"Estadiscas: \nPuntos Totales {estado_partida["puntaje"]} | Cantidad Errores {estado_partida["errores"]} | Nivel Alcanzado {estado_partida["nivel"]}")
        
