from datos import *
from funciones import *
from archivos import *
def manejo_niveles(estado_partida):
    if estado_partida["ganaste"]:
        if estado_partida["partida"] == 3:
            estado_partida["nivel"] +=1 
            estado_partida["partida"] =0
        estado_partida["partida"] +=1
    

def manejo_puntaje(estado_partida):
    estado_partida["puntaje_ronda"] = 0
    match estado_partida["comodines_usados"]:
        case 1:
            estado_partida["puntaje_ronda"] -= 20
        case 2:
            estado_partida["puntaje_ronda"] -= 40
        case 3:
            estado_partida["puntaje_ronda"] -= 60
    match estado_partida["intentos"]:
        case 1:
            estado_partida["puntaje_ronda"] += 300
        case 2:
            estado_partida["puntaje_ronda"] += 250
        case 3:
            estado_partida["puntaje_ronda"] += 200
        case 4:
            estado_partida["puntaje_ronda"] += 150
        case 5:
            estado_partida["puntaje_ronda"] += 100
        case 6:
            estado_partida["puntaje_ronda"] += 50
    color = GREEN
    if not estado_partida["ganaste"]:
        print("se te descontaran 100 puntos por no haber adivinado la palabra")
        estado_partida["puntaje_ronda"] -= 100
        
        if estado_partida["puntaje_ronda"] < 0:
            color = RED
    
    print(f"puntos ganados en la partida: {color}{estado_partida["puntaje_ronda"]}{RESET}\n")
    estado_partida["puntaje"] += estado_partida["puntaje_ronda"]

def manejo_vidas(estado_partida):
    if not estado_partida["ganaste"]:
        estado_partida["vidas"] -= 1
    return estado_partida["vidas"]

def menu(usuario: dict):
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

    #logueo
    #
    vidas=3
    errores=0
    intentos=0
    puntaje=0
    nivel= 1
    partida=1
    
    choice = mostrar_menu() 
    while  vidas != 0 and (partida <= 3 and nivel <= 3):
        comodines_usados=0
        match choice:
            case "1":
                
                #resultado_partida , intentos , intentos_fallidos, comodines_usados = jugar(nivel, partida , vidas, puntaje, comodines_usados)
                jugar(estado_partida)
                #errores += intentos_fallidos
                #puntaje , puntaje_ronda = manejo_puntaje(puntaje, intentos, comodines_usados , resultado_partida)
                manejo_puntaje(estado_partida)
                #vidas = manejo_vidas(vidas, resultado_partida)
                manejo_vidas(estado_partida)
                manejo_niveles(estado_partida)
                #actualizar_estadisticas(usuario["nombre"], puntaje_ronda, errores, nivel)
                actualizar_estadisticas(usuario["nombre"], estado_partida["puntaje_ronda"], estado_partida["errores"], estado_partida["nivel"])
            case "2":
                jugar_secreto(nivel, partida , vidas, puntaje)
            case "3":
                mostrar_instrucciones_juego()
                choice = mostrar_menu()
            case "4":
                print("Salir. ¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Intenta de nuevo.\n")
    finalizar_juego(vidas, puntaje, errores)

def finalizar_juego(vidas, puntaje, errores):
    if vidas == 0:
        print("perdiste mal ahi")
    else:
        print("sos todo crack ganaste")
        print(f"Estadiscas: \nPuntos Totales {puntaje} | Cantidad Errores {errores}")