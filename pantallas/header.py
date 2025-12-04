import pygame
def dibujar_fondo_barra(ventana: pygame.surface, config: dict) -> None:
    """Dibuja el fondo y los bordes de la barra superior.

    Args:
        ventana (pygame.surface): Ventana donde se dibuja.
        config (dict): Configuración del juego (ancho, alto, colores, etc).
    """
    barra = pygame.Rect(0, 0, config["ANCHO"], 55)
    pygame.draw.rect(ventana, (255, 242, 249), barra)
    pygame.draw.line(ventana, (255, 161, 212), (0, 0), (config["ANCHO"], 0), 2)
    pygame.draw.line(ventana, (255, 161, 212), (0, 55), (config["ANCHO"], 55), 2)
    
def crear_corazones_imagen(vidas: int, img_corazon: pygame.surface) -> list:
    """Calcula las posiciones donde deben dibujarse los corazones.

    Args:
        vidas (int): Cantidad de corazones a mostrar.
        img_corazon (pygame.surface): Imagen del corazón.

    Return:
        list: Lista con las posiciones en donde se dibujará cada corazón.
    
    """
    lista_posiciones = []
    i = 0
    x = 0

    an = img_corazon.get_width() + 5  # separación entre corazones

    while i < vidas:
        lista_posiciones.append(x)
        x = x + an
        i += 1

    return lista_posiciones

def dibujar_corazones(ventana: pygame.surface, img_corazon: pygame.surface, vidas: int, x: int, y: int, espacio: int = 35) -> None:
    """Dibuja los corazones según la cantidad de vidas.

    Args:
        ventana (pygame.surface): Ventana donde dibujar.
        img_corazon (pygame.surface): Imagen del corazón.
        vidas (int): Cantidad de corazones a mostrar.
        x (int): Posición X inicial.
        y (int): Posición Y inicial.
        espacio (int, optional): Separación entre corazones (por defecto 35).
    """
    i = 0
    while i < vidas:
        ventana.blit(img_corazon, (x + i * espacio, y))
        i += 1

def obtener_texto_categoria(estado: dict) -> str:
    """Devuelve la categoría si está revelada, o 'Tema: ???' si no.

    Args:
        estado (dict): Estado de la partida (tema revelado, categoría, etc).

    Returns:
        str: Texto de categoría para mostrar.
    """
    if estado["tema_revelado"]:
        return estado["categoria"]
    else:
        return "Tema: ???"

def crear_texto_barra(nivel: int, partida: int, categoria: str, puntos: int) -> str:
    """Crea el texto completo que aparece en la barra superior."""
    return f"Nivel {nivel} | Partida {partida} | {categoria} | Puntos: {puntos}"


def dibujar_barra_superior(ventana: pygame.surface, config: dict, estado: dict, datos: dict) -> None:
    """Dibuja toda la barra superior: fondo, texto y corazones.

    Args:
        ventana (pygame.surface): Ventana donde se dibuja.
        config (dict): Configuración general (ancho, alto, fuentes, etc).
        estado (dict): Estado gráfico (fuentes, imágenes, tema, etc).
        datos (dict): Datos de la partida (nivel, partida, vidas, etc).
    """
    dibujar_fondo_barra(ventana, config)

    categoria = obtener_texto_categoria(estado)

    # Texto centrado (usa nivel y partida desde datos)
    texto = crear_texto_barra
    texto = f"Puntos {datos["puntos_totales"]} | Nivel {datos['nivel']} | Partida {datos['partida']} | {categoria}"
    img_texto = estado["fuente_sub"].render(texto, True, (179, 0, 134))

    ventana.blit(img_texto, (15, 15))

    # Corazones desde datos["vidas"]
    dibujar_corazones( ventana, estado["img_corazon"], datos["vidas"], x=395, y=15)

