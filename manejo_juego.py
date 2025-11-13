from datos import *
from funciones import *
from archivos import *
def manejo_niveles(resultado_partida, nivel, partida):
    if resultado_partida:
        if partida == 3:
            nivel +=1 
            partida =0
        partida += 1
    return nivel, partida

def manejo_puntaje(puntaje, intentos, comodines_usados , resultado_partida):
    puntaje_ronda=0
    match comodines_usados:
        case 1:
            puntaje_ronda -= 20
        case 2:
            puntaje_ronda -= 40
        case 3:
            puntaje_ronda -= 60
    match intentos:
        case 1:
            puntaje_ronda += 300
        case 2:
            puntaje_ronda += 250
        case 3:
            puntaje_ronda += 200
        case 4:
            puntaje_ronda += 150
        case 5:
            puntaje_ronda += 100
        case 6:
            puntaje_ronda += 50
    color = GREEN
    if not resultado_partida:
        print("se te descontaran 100 puntos por no haber adivinado la palabra")
        puntaje_ronda -= 100
        
        if puntaje_ronda < 0:
            color = RED
    
    print(f"puntos ganados en la partida: {color}{puntaje_ronda}{RESET}\n")
    puntaje += puntaje_ronda
    return puntaje , puntaje_ronda

def manejo_vidas(vidas, resultado_partida):
    if not resultado_partida:
        vidas -= 1
    return vidas

def menu(usuario: dict):
    estado = {
    "nivel": 1,
    "partida": 1,
    "vidas": 3,
    "puntaje": 0,
    "comodines_usados": 0,
    "errores": 0,
    
    "intentos": 0,
    
    
    
    
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
                
                resultado_partida , intentos , intentos_fallidos, comodines_usados = jugar(nivel, partida , vidas, puntaje, comodines_usados)
                errores += intentos_fallidos
                puntaje , puntaje_ronda = manejo_puntaje(puntaje, intentos, comodines_usados , resultado_partida)
                vidas = manejo_vidas(vidas, resultado_partida)
                nivel, partida = manejo_niveles(resultado_partida, nivel, partida)
                actualizar_estadisticas(usuario["nombre"], puntaje_ronda, errores, nivel)
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