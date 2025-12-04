def pantalla_estadisticas(VENTANA, config: dict, estadisticas: dict) -> None:
    """Muestra la pantalla de estadísticas del jugador

    Args:
        VENTANA (pygame.surface): Ventana principal donde se dibuja todo.
        config (dict): Configuración general del juego (tamaño, fuentes, colores).
        estadisticas (dict): Diccionario con las estadísticas del jugador (puntaje, errores, niveles, tiempo).

    Funcionamiento:
        - Procesa el tiempo total jugado y lo convierte en formato minutos y segundos.
        - Carga el fondo de la pantalla y las fuentes configuradas.
        - Renderiza todas las estadísticas en pantalla.
        - Permite volver al menú presionando ESC.
        - Mantiene un loop principal hasta que el usuario salga.

    Returns:
        None
    """
    import pygame, sys

    # PROCESAR TIEMPO
    tiempo = estadisticas.get("tiempo_juegado", 0)
    tiempo_int = int(tiempo)

    minutos = tiempo_int // 60
    segundos = tiempo_int % 60

    tiempo_formateado = f"Tiempo: {minutos:02d}:{segundos:02d}"

    # CONFIG
    ANCHO = config["ANCHO"]
    ALTO = config["ALTO"]

    FUENTE_TIT = pygame.font.SysFont(*config["FUENTES"]["TITULO"])
    FUENTE_SUB = pygame.font.SysFont(*config["FUENTES"]["SUBTITULO"])

    colores = config["COLORES"]

    reloj = pygame.time.Clock()
    corriendo = True

    fondo = pygame.image.load("imagenes/Estadisticas Wordle.jpg").convert()

    # Lista de estadísticas sin el tiempo
    claves = [c for c in estadisticas.keys() if c != "tiempo_juegado"]

    while corriendo:
        VENTANA.fill(colores["BG"])
        VENTANA.blit(fondo, (0, 0))

        # MOSTRAR ESTADISTICAS
        y = 165
        salto = 40

        for clave in claves:
            valor = estadisticas[clave]
            texto = clave.replace("_", " ").title() + ": " + str(valor)

            r = FUENTE_SUB.render(texto, True, (179, 0, 134))
            VENTANA.blit(r, (60, y))
            y += salto

        # MOSTRAR TIEMPO (como otra línea más)
        r_tiempo = FUENTE_SUB.render(tiempo_formateado, True, (179, 0, 134))
        VENTANA.blit(r_tiempo, (60, y))

        # VOLVER
        volver = FUENTE_SUB.render(
            "Presiona ESC para volver al menú", True, (179, 0, 134)
        )
        VENTANA.blit(volver, (ANCHO // 2 - volver.get_width() // 2, ALTO - 60))

        # EVENTOS
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                corriendo = False

            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        reloj.tick(60)
