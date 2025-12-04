import pygame
import random

def popup_general(ventana: pygame.surface, estado: dict, titulo: str, color_titulo: tuple, color_borde: tuple):
    """Dibuja un popup genérico para mostrar mensajes como 'Ganaste', 'Perdiste', etc.

    Args:
        ventana (pygame.surface): Ventana principal.
        estado (dict): Contiene palabra, fuentes y colores.
        titulo (str): Texto a mostrar como encabezado.
        color_titulo (tuple): Color RGB del título.
        color_borde (tuple): Color RGB del borde.

    Returns:
        None
    """
    popup = pygame.Surface((360, 190))
    popup.fill((255, 242, 249))  # fondo pastel más clarito
    pygame.draw.rect(popup, color_borde, (0, 0, 360, 190), 4, border_radius=18)

    t1 = estado["fuente_tit"].render(titulo, True, color_titulo)
    t2 = estado["fuente_sub"].render("La palabra era:", True, estado["colores_grilla"]["NEGRO"])
    t3 = estado["fuente_tit"].render(estado["palabra"], True, estado["colores_grilla"]["NEGRO"])

    popup.blit(t1, (175 - t1.get_width() // 2, 15))
    popup.blit(t2, (175 - t2.get_width() // 2, 70))
    popup.blit(t3, (175 - t3.get_width() // 2, 110))

    ventana.blit(popup, (75, 210))
    pygame.display.update()
    pygame.time.delay(2300)


def popup_gano(ventana: pygame.surface, estado: dict) -> None:
    """Popup que muestra 'Ganaste'.

    Args:
        ventana (pygame.surface): Ventana principal.
        estado (dict): Contiene palabra, fuentes y colores.

    Returns:
        None
    """
    
    titulo = "¡Ganaste!"
    color_titulo = (42, 166, 62)
    color_borde = (42, 166, 62)

    popup_general(
        ventana,
        estado,
        titulo,
        color_titulo,
        color_borde
    )


def popup_perdio(ventana: pygame.surface, estado: dict) -> None:
    """Popup que muestra 'Perdiste'.

    Args:
        ventana (pygame.surface): Ventana principal
        estado (dict): Contiene palabra, fuentes y colores.

    Returns:
        None
    """
    titulo = "¡Perdiste!"
    color_titulo = (255, 99, 126)
    color_borde = (255, 99, 126)

    popup_general(
        ventana,
        estado,
        titulo,
        color_titulo,
        color_borde
    )

def popup_login_exitoso(ventana: pygame.surface, usuario, fuente_tit, fuente_sub, colores: dict) -> None:
    """Popup que indica que el usuario inició sesión correctamente.

    Args:
        ventana (pygame.surface): Ventana del juego.
        usuario (str): Nombre del usuario.
        fuente_tit (pygame.font.Font): Fuente del título.
        fuente_sub (pygame.font.Font): Fuente del texto.
        colores (dict): Colores disponibles.
    """
    titulo = "¡Sesión iniciada!"
    color_titulo = (81, 162, 255)
    color_borde = (219, 234, 254)

    popup_general(
        ventana,
        usuario,
        fuente_tit,
        fuente_sub,
        colores,
        titulo,
        color_titulo,
        color_borde
    )

def popup_mensaje(ventana, mensaje, fuente_tit, fuente_sub, colores, titulo="Mensaje", color_titulo=(179, 0, 134), color_borde=(255, 161, 212)):
    """
    Muestra un popup con un mensaje personalizado.

    Args:
        ventana (Surface): Ventana principal.
        mensaje (str): Texto del mensaje.
        fuente_tit (Font): Fuente del título.
        fuente_sub (Font): Fuente del texto.
        colores (dict): Diccionario de colores.
        titulo (str): Título del popup.
        color_titulo (tuple): Color RGB del título.
        color_borde (tuple): Color RGB del borde.

    Returns:
        None
    """
    popup = pygame.Surface((360, 190))
    popup.fill((255, 242, 249))
    pygame.draw.rect(popup, color_borde, (0, 0, 360, 190), 4, border_radius=18)

    t1 = fuente_tit.render(titulo, True, color_titulo)
    popup.blit(t1, (180 - t1.get_width() // 2, 15))

    t2 = fuente_sub.render(mensaje, True, (179, 0, 13))
    popup.blit(t2, (180 - t2.get_width() // 2, 100))

    ventana.blit(popup, (ventana.get_width()//2 - 180, ventana.get_height()//2 - 95))
    pygame.display.update()
    pygame.time.delay(2500)


def popup_revelar_letra(ventana: pygame.surface, secreto: str, fuente_tit: tuple, fuente_sub: tuple, colores: dict, desorden: bool = False) -> str:
    """
    Muestra un popup en Pygame revelando una letra del secreto.

    Args:
        ventana (pygame.Surface): Ventana principal.
        secreto (str): Palabra secreta.
        fuente_tit (tuple): Tupla (nombre_fuente, tamaño) para fuente principal.
        fuente_sub (tuple): Tupla (nombre_fuente, tamaño) para fuente secundaria.
        colores (dict): Diccionario con colores.
        desorden (bool): Si es True, muestra la letra en posición aleatoria distinta.

    Returns:
        str: La letra revelada.
    """
    fuente_tit_obj = pygame.font.SysFont(*fuente_tit)
    fuente_sub_obj = pygame.font.SysFont(*fuente_sub)

    letra, posicion = letra_aleatoria(secreto)
    if desorden:
        posicion_aleatoria = random.randint(0, len(secreto)-1)
        while posicion_aleatoria == posicion:
            posicion_aleatoria = random.randint(0, len(secreto)-1)
    else:
        posicion_aleatoria = posicion

    popup_w, popup_h = 360, 190
    popup = pygame.Surface((popup_w, popup_h))
    popup.fill((255, 250, 220))
    color_borde = (200, 200, 100)
    pygame.draw.rect(popup, color_borde, (0, 0, popup_w, popup_h), 4, border_radius=18)


    titulo = "¡Comodín: Letra revelada!"
    t1 = fuente_tit_obj.render(titulo, True, (100, 100, 50))
    popup.blit(t1, (popup_w//2 - t1.get_width()//2, 15))

    t2 = fuente_sub_obj.render("La letra es:", True, (179, 0, 13))
    popup.blit(t2, (popup_w//2 - t2.get_width()//2, 70))


    letra_textos = []
    for i in range(len(secreto)):
        if i == posicion_aleatoria:
            color = colores["AMARILLO"] if desorden else colores["VERDE"]
            char = letra
        else:
            color = colores["GRIS_CLARO"]
            char = "X"
        letra_textos.append(fuente_tit_obj.render(char, True, color))

    start_x = popup_w//2 - (len(secreto)*40)//2
    y_pos = 110
    for i, text in enumerate(letra_textos):
        popup.blit(text, (start_x + i*40, y_pos))

    ventana.blit(popup, (75, 210))
    pygame.display.update()
    pygame.time.delay(1200)

    return letra


def letra_aleatoria(palabra: str) -> tuple[str, int]:
    """Devuelve una letra aleatoria de la palabra y su posición.

    Returns:
        tuple[str, int]: (letra, índice).
    """
    indice = random.randrange(len(palabra))
    return palabra[indice], indice

