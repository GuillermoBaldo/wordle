import pygame
import sys
def pantalla_instrucciones(VENTANA: pygame.surface, config: dict) -> None:
    """Muestra la pantalla de instrucciones del juego Wordle.
        Explica reglas visualmente, muestra ejemplos de colores y espera a que el usuario presione ESC para volver al menú.

    Args:
        VENTANA (pygame.surface): Ventana del juego donde se dibuja todo.
        config (dict): Configuraciones generales (coloresm fuentes, tamaños, etc).

    Returns:
        None
    """
    ANCHO = config["ANCHO"]
    ALTO = config["ALTO"]

    FUENTE_TIT = pygame.font.SysFont(*config["FUENTES"]["TITULO"])
    FUENTE_SUB = pygame.font.SysFont(*config["FUENTES"]["SUBTITULO"])
    FUENTE_LETRA = pygame.font.SysFont("arial", 28)

    colores = config["COLORES"]

    fondo = pygame.image.load("imagenes/Instrucciones Wordle.jpg")

    reloj = pygame.time.Clock()

    ejemplo = ["A", "R", "B", "O", "L"]
    estados = ["verde", "amarillo", "gris", "verde", "gris"]

    corriendo = True

    while corriendo:
        VENTANA.blit(fondo, (0, 0))


        sub = FUENTE_SUB.render("Adiviná la palabra en solo 6 intentos!", True, (179, 0, 134))
        VENTANA.blit(sub, (ANCHO//2 - sub.get_width()//2, 90))

        sub2 = FUENTE_SUB.render("Los colores indican qué tan cerca estás:", True, (179, 0, 134))
        VENTANA.blit(sub2, (ANCHO//2 - sub2.get_width()//2, 115))

        size = 60
        espacio = 10
        x_ini = ANCHO//2 - (size*5 + espacio*4)//2
        y_ini = 170

        i = 0
        while i < 5:
            estado = estados[i]

            if estado == "verde":
                color = (187, 244, 81)
            elif estado == "amarillo":
                color = (255, 240, 133)
            else:
                color = (212, 212, 212)

            rect = pygame.Rect(x_ini + i*(size+espacio), y_ini, size, size)

            pygame.draw.rect(VENTANA, color, rect, border_radius=5)
            pygame.draw.rect(VENTANA, (179, 0, 134), rect, 3, border_radius=10)

            letra = FUENTE_LETRA.render(ejemplo[i], True, (179, 0, 134))
            VENTANA.blit(
                letra,
                (rect.centerx - letra.get_width()//2,
                rect.centery - letra.get_height()//2)
            )

            i = i + 1

        exp1 = FUENTE_SUB.render("VERDE: Letra correcta en la posición correcta.", True, (179, 0, 134))
        VENTANA.blit(exp1, (ANCHO//2 - exp1.get_width()//2, 270))

        exp2 = FUENTE_SUB.render("AMARILLO: Letra en la palabra, pero en otra posición.", True, (179, 0, 134))
        VENTANA.blit(exp2, (ANCHO//2 - exp2.get_width()//2, 300))

        exp3 = FUENTE_SUB.render("GRIS: La letra no está en la palabra.", True, (179, 0, 134))
        VENTANA.blit(exp3, (ANCHO//2 - exp3.get_width()//2, 330))

        volver = FUENTE_SUB.render("Presiona ESC para volver al menú", True, (179, 0, 134))
        VENTANA.blit(volver, (ANCHO // 2 - volver.get_width() // 2, ALTO - 60))


        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    corriendo = False

            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        reloj.tick(60)

    return

