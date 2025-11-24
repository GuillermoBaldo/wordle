from mostrar_datos import *
from manejoJSON import *
from manejoCSV import *
from manejo_juego import *
from partidas import *
import time

def menu(usuario: dict) -> None:
    """Controla el flujo del juego, mostrando el menú y ejecutando las opciones seleccionadas.

    Args:
        usuario (dict): Datos del usuario logueado.

    Returns:
        None
    """
    inicio = time.time()
    estado_partida, palabras, config= inicializar_partida()
    choice = mostrar_menu() 
    while  estado_partida["vidas"] != 0 and (estado_partida["partida"] <= int(config["MAX_PARTIDAS"])) and estado_partida["nivel"] <= int(config["MAX_NIVELES"]):
        match choice:
            case "1":
                resumen_nivel(estado_partida, config)
                jugar(estado_partida, palabras, config)
                manejo_puntaje(estado_partida, config)
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
    
    config = cargar_config("/Users/guille/Documents/computacion/wordle/archivos/config.csv")

    return estado_partida , palabras , config

def resumen_nivel(estado_partida: dict, config) -> None:
    """Muestra el resumen estadístico cuando el jugador pasa de nivel.

    Args:
        estado_partida (dict): Estado de la partida.

    Returns:
        None
    """
    if estado_partida["nivel"] >1 and estado_partida["partida"] == 1:
        print(f"{config["GREEN"]}Felicidades has pasado al nivel {estado_partida["nivel"]}!{config["RESET"]}")
        print("las estadisticas de tu partida son las siguientes:")
        print(f"Puntos Totales {estado_partida["puntaje"]} | Cantidad Errores {estado_partida["errores"]} | Nivel Alcanzado {estado_partida["nivel"] -1 }")
        

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
        