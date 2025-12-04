import pygame
import sys
from inicializar_partida import *
from pantallas.header import *
from funciones_espesificas import *
from recursos_juego.boton import *
from recursos_juego.popup import *
from recursos_juego.grilla import *
def daltonismo(estado, config, evento):
    if estado["datos_imagen"][1].collidepoint(evento.pos):
        sonido_click = pygame.mixer.Sound(config["sonido"]["CLICK"])
        sonido_click.set_volume(0.5)
        sonido_click.play()

        if config["DALTONISMO"] == False:
            config["DALTONISMO"]= True
            
        elif config["DALTONISMO"] == True:
            config["DALTONISMO"]= False
            

def manejar_click_mouse(evento, ventana, config, estado):
    terminar = False
    
    sonido_click = pygame.mixer.Sound(config["sonido"]["CLICK"])
    sonido_click.set_volume(0.5)

    # Botón revelar tema
    if boton_fue_presionado(estado["botones"][1], evento):
        sonido_click.play()
        estado["tema_revelado"] = True

    # Botón comodín 1
    elif boton_fue_presionado(estado["botones"][0], evento):
        sonido_click.play()
        usar_comodin(estado, ventana, config, "comdin_usado1", False)

    # Botón comodín 2
    elif boton_fue_presionado(estado["botones"][2], evento):
        sonido_click.play()
        usar_comodin(estado, ventana, config, "comdin_usado2", True)

    return terminar

def manejar_teclas(evento, ventana, config, estado):
    terminar = False

    if evento.key == pygame.K_ESCAPE:
        perder_por_escape(estado)
        terminar = True

    elif evento.key == pygame.K_BACKSPACE:
        borrar_letra(estado)

    elif pygame.K_a <= evento.key <= pygame.K_z:
        escribir_letra(evento, estado)

    elif evento.key == pygame.K_RETURN:
        if procesar_enter(ventana, config, estado):
            terminar = True

    return terminar

def procesar_enter(ventana, config, estado):
    terminar = False
    

    if estado["pos_letra"] != 5:
        return terminar

    colorear_intento(estado)

    if verificar_ganador(estado):
        puntos_intentos(estado)
        popup_gano(ventana, estado)
        estado["resultado"] = "gano"
        estado["puntos_finales"] = estado["puntos"]
        estado["terminar"] = True
        terminar = True

    else:
        estado["errores_totales"] += 1
        estado["intento_actual"] += 1
        estado["pos_letra"] = 0

        if estado["intento_actual"] >= 6:
            estado["puntos"] = 0
            popup_perdio(ventana, estado)
            estado["resultado"] = "perdio"
            estado["terminar"] = True
            terminar = True

    return terminar

def usar_comodin(estado, ventana, config, clave, permitir_ubicacion):
    fuente_tit = pygame.font.SysFont(*config["FUENTES"]["TITULO"])
    fuente_sub = pygame.font.SysFont(*config["FUENTES"]["SUBTITULO"])
    colores = config["COLORES"]

    if not estado.get(clave, False):
        estado[clave] = True
        revelar_letra_grilla(estado, permitir_ubicacion)
    else:
        popup_mensaje(
            ventana,
            "Solo un uso por partida!! >_<",
            fuente_tit,
            fuente_sub,
            colores,
            titulo="¡Comodín ya usado!"
        )
        
def perder_por_escape(estado):
    """El jugador se rinde usando ESC."""
    estado["terminar"] = True
    estado["resultado"] = "perdio"
    estado["puntos_finales"] = estado["puntos"]

def borrar_letra(estado):
    """Borra la última letra escrita si hay lugar."""
    if estado["pos_letra"] > 0:
        estado["pos_letra"] -= 1
        estado["intentos"][estado["intento_actual"]][estado["pos_letra"]] = ""


def escribir_letra(evento, estado):
    """Escribe una letra si aún no se completaron las 5 casillas."""
    if estado["pos_letra"] < 5:
        estado["intentos"][estado["intento_actual"]][estado["pos_letra"]] = evento.unicode.upper()
        estado["pos_letra"] += 1

def puntos_intentos(estado: dict) -> None:
    """Asigna puntos según la cantidad de intentos usados.
        Más rápido adivina, más puntos.

    Args:
        estado (dict): Estado actual de la partida, contiene 'intento_actual' y 'puntos'.

    Returns:
        None
    """
    puntos= 50
    print(estado["intento_actual"])
    match estado["intento_actual"]:
        case 0:
            estado["puntos"] = puntos*6
        case 1:
            estado["puntos"] = puntos*5
        case 2:
            estado["puntos"] = puntos*4
        case 3:
            estado["puntos"] = puntos*3
        case 4:
            estado["puntos"] = puntos*2
        case 5:
            estado["puntos"] = puntos*1
            
