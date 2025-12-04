import pygame
def crear_input(x, y, w, h, placeholder="", password=False):
    """Crea un diccionario que representa un campo de texto (input).

    Args:
        x (int): Posición X del input.
        y (int): Posición Y del input.
        w (int): Ancho del input.
        h (int): Alto del input.
        placeholder (str): Texto que se muestra cuando está vacío. 
        password (bool): Si es True, se muestran asteriscos.

    Returns:
        dict: Estructura con toda la información del input.
    """
    return {
        "rect": pygame.Rect(x, y, w, h),
        "texto": "",
        "activa": False,
        "placeholder": placeholder,
        "password": password
    }


def dibujar_input(caja: dict, ventana: pygame.surface, config: dict) -> None:
    """Dibuja el input en pantalla.

    Args:
        caja (dict): El input creado por crear_input()
        ventana (pygame.surface): Superficie donde se dibuja.
        config (dict): Configuración general del juego.

    Returns:
        None
    """
    fuente_input = pygame.font.SysFont(*config["FUENTES"]["INPUT"])
    x, y, w, h = caja["rect"]

    fondo = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.rect(fondo, (255, 255, 255, 180), (0, 0, w, h), border_radius=12)
    ventana.blit(fondo, (x, y))

    pygame.draw.rect(ventana, (200, 200, 200), caja["rect"], 2, border_radius=12)

    if caja["texto"] == "" and not caja["activa"]:
        texto_surf = fuente_input.render(caja["placeholder"], True, (140, 140, 140))
    else:
        contenido = caja["texto"]
        if caja["password"]:
            contenido = "*" * len(contenido)
        texto_surf = fuente_input.render(contenido, True, (60, 60, 60))

    ventana.blit(texto_surf, (x + 12, y + 12))



def manejar_input_evento(caja: dict, evento) -> None:
    """Procesa los eventos del teclado y mouse para el input.

    Args:
        caja (dict): El input a modificar.
        evento (Event): Evento.

    Returns:
        None
    """
    sonido_click = pygame.mixer.Sound("sonidos/typing-sound-02-229861.mp3")
    sonido_click.set_volume(0.5)
    if evento.type == pygame.MOUSEBUTTONDOWN:
        caja["activa"] = caja["rect"].collidepoint(evento.pos)

    if evento.type == pygame.KEYDOWN and caja["activa"]:
        sonido_click.play()
        if evento.key == pygame.K_BACKSPACE:
            caja["texto"] = caja["texto"][:-1]
        elif evento.key != pygame.K_RETURN:
            caja["texto"] += evento.unicode