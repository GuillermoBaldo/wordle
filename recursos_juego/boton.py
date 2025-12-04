import pygame
def dibujar_botones(botones: list, fuente: tuple = ("Arial", 30)):
    """Dibuja todos los botones en pantalla."""
    for boton in botones:
        dibujar_boton(boton, fuente)
        
def crear_boton(ventana: pygame.Surface, dimensiones: tuple, posicion: tuple,
                path_imagen: str = None, fuente: tuple = ("arial", 7),
                texto: str = None) -> dict:
    """Crea un botón interactivo para la interfaz del juego.

    Args:
        ventana (pygame.Surface): Superficie donde se dibuja el botón.
        dimensiones (tuple): Tamaño del botón (ancho, alto).
        posicion (tuple): Posición superior izquierda del botón (x, y).
        path_imagen (str, optional): Ruta a una imagen opcional para usar como fondo del botón. Si es None, el botón se dibuja con un rectángulo gris.
        fuente (tuple, optional): None y tamaño de la fuente a usar para el texto.
        texto (str, optional): Texto que se mostrará dentro del botón. Si es None, no se dibuja texto.

    Returns:
        dict: Diccionario que representa el botón, incluyendo:
                - superficie (pygame.surface): imagen del botón
                - rectángulo (pygame.rect): área clickeable
                - fuente (pygame.font.font)
                - texto, ancho, alto, posición, etc.
    """
    boton = {
        "ventana": ventana,
        "ancho": dimensiones[0],
        "alto": dimensiones[1],
        "posicion": posicion,
        "presionado": False,
        "texto": texto,
        "rectangulo": pygame.Rect(posicion[0], posicion[1], dimensiones[0], dimensiones[1])
    }

    if path_imagen is not None:
        imagen = pygame.image.load(path_imagen).convert_alpha()
        boton["superficie"] = pygame.transform.scale(imagen, dimensiones)
    else:
        superficie = pygame.Surface(dimensiones)
        superficie.fill((230, 230, 230))
        boton["superficie"] = superficie

    nombre_fuente, tamaño = fuente
    boton["fuente"] = pygame.font.SysFont(nombre_fuente, tamaño)

    return boton

def dibujar_boton(boton: dict, fuente: tuple = ("Arial", 30)):
    ventana = boton["ventana"]
    x, y = boton["posicion"]
    w, h = boton["ancho"], boton["alto"]
    tipo_fuente, tamaño_fuente = fuente
    radio = 40

    grad = pygame.Surface((w, h))
    for i in range(h):
        r = 255
        g = int(120 - 90 * (i / h))
        b = int(200 + 40 * (i / h))
        pygame.draw.line(grad, (r, g, b), (0, i), (w, i))

    grad = grad.convert_alpha()

    mask = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.rect(mask, (255, 255, 255), (0, 0, w, h), border_radius=radio)
    grad.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    ventana.blit(grad, (x, y))
    pygame.draw.rect(ventana, (255, 255, 255), (x, y, w, h), width=4, border_radius=radio)

    fuente = pygame.font.SysFont(tipo_fuente, tamaño_fuente, bold=True)
    texto_surf = fuente.render(boton["texto"], True, (255, 255, 255))
    ventana.blit(
        texto_surf,
        (
            x + w//2 - texto_surf.get_width()//2,
            y + h//2 - texto_surf.get_height()//2
        )
    )


def boton_fue_presionado(boton: dict, evento: pygame.event.Event) -> bool:
    fue_presionado = False

    if evento.type == pygame.MOUSEBUTTONDOWN:
        if boton["rectangulo"].collidepoint(evento.pos):
            boton["presionado"] = True
            fue_presionado = True
        else:
            boton["presionado"] = False

    return fue_presionado

