import pygame
import sys
from manejoCSV import *
from recursos_juego.boton import  boton_fue_presionado
from pantallas.pantalla_jugar import *
from manejoJSON import *
from logica_juego import *
from recursos_juego.recurso_menu import *

def procesar_eventos_menu(evento, estado, recursos, config, usuario, ventana):
    if evento.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if evento.type == pygame.MOUSEBUTTONDOWN:

        # --- Control de sonido ---
        manejar_click_boton_sonido(evento,estado, recursos)

        # --- Botones ---
        botones = estado["botones"]
        if boton_fue_presionado(botones[0], evento):
            recursos["sonido_click"].play()
            ejecutar_jugar(config, usuario, recursos, ventana)

        elif boton_fue_presionado(botones[1], evento):
            recursos["sonido_click"].play()
            ejecutar_instrucciones(config, ventana, recursos)

        elif boton_fue_presionado(botones[2], evento):
            recursos["sonido_click"].play()
            ejecutar_estadisticas(config, ventana, usuario, recursos)


def pantalla_menu_principal(ventana: pygame.surface, config: dict, usuario: dict):
    reloj = pygame.time.Clock()
    recursos = cargar_recursos_menu(config)
    estado_menu = crear_estado_menu(ventana, config, recursos)
    corriendo = True
    
    while corriendo:
        for evento in pygame.event.get():
            procesar_eventos_menu(evento,estado_menu,recursos,config,usuario,ventana)

        dibujar_menu(ventana,config,usuario,recursos,estado_menu)

        pygame.display.update()
        reloj.tick(60)

