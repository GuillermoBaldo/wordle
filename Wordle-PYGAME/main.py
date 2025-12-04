import pygame
from manejoJSON import *
from pantallas.pantalla_menu import pantalla_menu_principal
from pantallas.pantalla_login import pantalla_login

def inicializar_pygame(config: dict):
    pygame.init()
    pygame.mixer.init()

    # Música
    pygame.mixer.music.load(config["sonido"]["MUSICA"])
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # Ventana
    ventana = pygame.display.set_mode((config["ANCHO"], config["ALTO"]))
    pygame.display.set_caption(config["TITULO_VENTANA"])
    pygame.display.set_icon(pygame.image.load("imagenes/Wordle ICON.png"))

    return ventana


def main():
    CONFIG = cargar_config()
    VENTANA = inicializar_pygame(CONFIG)
    usuario = pantalla_login(VENTANA, CONFIG)
    print(f"Usuario logueado: {usuario}")
    pantalla_menu_principal(VENTANA, CONFIG, usuario)


if __name__ == "__main__":
    main()
