from datos import *
from funciones import *
from manejoJSON import *
import time

def manejo_niveles(estado_partida):
    if estado_partida["ganaste"]:
        if estado_partida["partida"] == 3:
            estado_partida["nivel"] +=1 
            estado_partida["partida"] =0
        estado_partida["partida"] +=1
    
def manejo_puntaje_x_comodines (estado_partida, puntos_x_comodin):
    match estado_partida["comodines_usados"]:
        case 1:
            estado_partida["puntaje_ronda"] -= puntos_x_comodin
        case 2:
            estado_partida["puntaje_ronda"] -= puntos_x_comodin * 2
        case 3:
            estado_partida["puntaje_ronda"] -= puntos_x_comodin * 3

def manejo_puntaje_x_intentos (estado_partida, puntos_x_intento):
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

def manejo_puntaje_derrota(estado_partida, puntos_x_perdida):
    if not estado_partida["ganaste"]:
        print(f"se te descontaran {puntos_x_perdida} puntos por no haber adivinado la palabra")
        estado_partida["puntaje_ronda"] -= puntos_x_perdida
    
def manejo_puntaje(estado_partida, puntos_x_comodin = 20, puntos_x_intento = 50 , puntos_x_perdida = 100 ):
    estado_partida["puntaje_ronda"] = 0
    
    manejo_puntaje_x_comodines(estado_partida, puntos_x_comodin)
    manejo_puntaje_x_intentos(estado_partida, puntos_x_intento)
    manejo_puntaje_derrota(estado_partida, puntos_x_perdida)
    color = GREEN
    
    if estado_partida["puntaje_ronda"] < 0:
        color = RED
    
    print(f"puntos ganados en la partida: {color}{estado_partida["puntaje_ronda"]}{RESET}\n")
    estado_partida["puntaje"] += estado_partida["puntaje_ronda"]

def manejo_vidas(estado_partida):
    if not estado_partida["ganaste"]:
        estado_partida["vidas"] -= 1
    return estado_partida["vidas"]

def resumen_nivel(estado_partida):
    if estado_partida["nivel"] >1 and estado_partida["partida"] == 1:
        print(f"{GREEN}Felicidades has pasado al nivel {estado_partida["nivel"]}!{RESET}")
        print("las estadisticas de tu partida son las siguientes:")
        print(f"Puntos Totales {estado_partida["puntaje"]} | Cantidad Errores {estado_partida["errores"]} | Nivel Alcanzado {estado_partida["nivel"] -1 }")
                
def menu(usuario: dict):
    inicio = time.time()
    estado_partida = inicializar_partida()
    choice = mostrar_menu() 
    while  estado_partida["vidas"] != 0 and (estado_partida["partida"] <= 3 and estado_partida["nivel"] <= 3):
        match choice:
            case "1":
                resumen_nivel(estado_partida)
                jugar(estado_partida)
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
    fin = time.time()
    finalizar_juego(estado_partida, inicio, fin)

def inicializar_partida():
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
    return estado_partida
    
def finalizar_juego(estado_partida, inicio, fin):
    if estado_partida["vidas"] == 0:
        print("perdiste mal ahi")
    else:
        print("sos todo crack ganaste")
        total_segundos = fin - inicio

        minutos = total_segundos // 60     # división entera, no usa int()
        segundos = total_segundos % 60     # resto

        print(f"Tiempo total: {minutos:.0f} min {segundos:.2f} seg")
        print(f"Estadiscas: \nPuntos Totales {estado_partida["puntaje"]} | Cantidad Errores {estado_partida["errores"]} | Nivel Alcanzado {estado_partida["nivel"]}")