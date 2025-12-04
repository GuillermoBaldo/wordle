import pygame
import sys
from inicializar_partida import *
from pantallas.header import *
from funciones_espesificas import *
from recursos_juego.boton import *
from recursos_juego.popup import *
from recursos_juego.grilla import *
from recursos_juego.recursos_juego import *

def procesar_eventos(ventana, config, estado):
    """Procesa eventos y devuelve True si el juego debe terminar."""
    terminar = False

    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            daltonismo(estado,config, evento)
            if manejar_click_mouse(evento, ventana, config, estado):
                terminar = True
            

        elif evento.type == pygame.KEYDOWN:
            if manejar_teclas(evento, ventana, config, estado):
                terminar = True
        
        

    return terminar


def pantalla_jugar(ventana: pygame.surface, config: dict, palabras: list, datos: dict) -> tuple:
    """Controla el ciclo principal de la pantalla de juego.
        Inicializa la partida, dibuja la interfaz, procesa eventos y devuelve el resultado final.

    Args:
        ventana (pygame.surface): Ventana principal del juego.
        config (dict): Configuración del programa.
        palabras (list): Lista de palabras posibles.
        datos (dict): Información del jugador (nivel, partida, vidas, etc).

    Returns:
        tuple:
            - resultado ('ganó' o 'perdió')
            - puntos finales obtenidos
            - errores totales cometidos
    """
    estado = inicializar_partida(ventana, config, palabras, datos)
    fondo = pygame.image.load("imagenes/Juego Wordle.jpg").convert()
    
    while not estado["terminar"]:
        ventana.blit(fondo, (0, 0))
        ventana.blit(estado["datos_imagen"][0], estado["datos_imagen"][1])
        
        dibujar_barra_superior(ventana ,config, estado, datos)
        dibujar_grilla(ventana, config, estado)
        dibujar_botones(estado["botones"], config["FUENTES"]["ESTADISTICAS"])
        procesar_eventos(ventana, config, estado)

        pygame.display.update()
        estado["reloj"].tick(60)
    
    
    return estado["resultado"], estado["puntos"], estado["errores_totales"]


