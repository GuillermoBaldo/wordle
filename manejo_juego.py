from funciones import *
from manejoJSON import *
from manejoCSV import *
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

def manejo_vidas(estado_partida):
    if not estado_partida["ganaste"]:
        estado_partida["vidas"] -= 1
    return estado_partida["vidas"]

def resumen_nivel(estado_partida):
    config = importar_configuracion("/Users/guille/Documents/computacion/wordle/archivos/config.csv")
    if estado_partida["nivel"] >1 and estado_partida["partida"] == 1:
        print(f"{config["GREEN"]}Felicidades has pasado al nivel {estado_partida["nivel"]}!{config["RESET"]}")
        print("las estadisticas de tu partida son las siguientes:")
        print(f"Puntos Totales {estado_partida["puntaje"]} | Cantidad Errores {estado_partida["errores"]} | Nivel Alcanzado {estado_partida["nivel"] -1 }")
                
def menu(usuario: dict):
    inicio = time.time()
    estado_partida , palabras= inicializar_partida()
    config = importar_configuracion("/Users/guille/Documents/computacion/wordle/archivos/config.csv")
    choice = mostrar_menu() 
    print(type(config["MAX_PARTIDAS"]))
    while  estado_partida["vidas"] != 0 and (estado_partida["partida"] <= 3 and estado_partida["nivel"] <= 3):
    #while  estado_partida["vidas"] != 0 and (estado_partida["partida"] <= config["MAX_PARTIDAS"] and estado_partida["nivel"] <= config["MAX_NIVELES"]):
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
    palabras=cargar_palabrasv2("/Users/guille/Documents/computacion/wordle/archivos/palabras (1).csv")

    return estado_partida , palabras
    
def finalizar_juego(estado_partida, inicio, fin):
    if estado_partida["vidas"] == 0:
        print("perdiste mal ahi")
    else:
        print("sos todo crack ganaste")
        total_segundos = fin - inicio

        minutos = total_segundos // 60     
        segundos = total_segundos % 60     

        print(f"Tiempo total: {minutos:.0f} min {segundos:.2f} seg")
        print(f"Estadiscas: \nPuntos Totales {estado_partida["puntaje"]} | Cantidad Errores {estado_partida["errores"]} | Nivel Alcanzado {estado_partida["nivel"]}")
        
