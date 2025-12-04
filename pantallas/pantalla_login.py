import pygame
import sys
from recursos_juego.boton import crear_boton, dibujar_boton, boton_fue_presionado
from login import login_usuario, registrar_usuario
from recursos_juego.inputbox import *
from recursos_juego.popup import *

# PANTALLA LOGIN CON FONDO
def pantalla_login(ventana: pygame.surface, config: dict) -> dict | None:
    """Muestra la pantalla de inicio de sesión del juego.
        Permite al usuario ingresar nombre y contraseña, iniciar sesión o crear un nuevo usuario.

    Args:
        ventana (pygame.surface): Ventana principal del juego.
        config (dict): Configuración del juego (dimensiones, fuentes, colores, sonido).

    Returns:
        dict | None:
            - Diccionario con los datos del usuario logueado si el login fue exitoso.
            - None si no se inició sesión.
    """
    ANCHO = config["ANCHO"]
    ALTO = config["ALTO"]

    fondo = pygame.image.load("imagenes/Wordle Login.jpg").convert()

    fuente_tit = pygame.font.SysFont(*config["FUENTES"]["TITULO"])
    fuente_sub = pygame.font.SysFont(*config["FUENTES"]["SUBTITULO"])
    colores = config["COLORES"]

    reloj = pygame.time.Clock()

    sonido_click = pygame.mixer.Sound(config["sonido"]["CLICK"])
    sonido_click.set_volume(0.5)

    panel_w, panel_h = 360, 360
    panel_x = ANCHO // 2 - panel_w // 2
    panel_y = ALTO // 2 - panel_h // 2 + 40

    # INPUTS
    caja_usuario = crear_input(panel_x + 25, panel_y + 50, 320, 50, "Usuario")
    caja_pass = crear_input(panel_x + 25, panel_y + 130, 320, 50, "Contraseña", password=True)

    # BOTONES
    boton_login = crear_boton(ventana, (320, 55), (panel_x + 25, panel_y + 195), texto="Iniciar Sesión")
    boton_registrar = crear_boton(ventana, (320, 55), (panel_x + 25, panel_y + 270), texto="Crear Usuario")

    en_login = True
    usuario_logueado = None

    while en_login:

        ventana.blit(fondo, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            manejar_input_evento(caja_usuario, evento)
            manejar_input_evento(caja_pass, evento)

            # LOGIN
            if boton_fue_presionado(boton_login, evento):
                sonido_click.play()
                usuario = login_usuario(caja_usuario["texto"], caja_pass["texto"])
                if usuario is not None:
                    popup_mensaje(ventana, "Sesión iniciada correctamente", fuente_tit, fuente_sub, colores, titulo="Inicio de sesión")
                    
                    usuario_logueado = usuario
                    en_login = False
                else:
                    popup_mensaje(ventana, "Usuario o contraseña incorrecta", fuente_tit, fuente_sub, colores, titulo="Error",)

            # REGISTRAR USUARIO
            if boton_fue_presionado(boton_registrar, evento):
                sonido_click.play()
                nuevo_usuario = registrar_usuario(caja_usuario["texto"], caja_pass["texto"])
                print(nuevo_usuario)
                if nuevo_usuario :
                    popup_mensaje(ventana,"Usuario creado exitosamente" , fuente_tit, fuente_sub, colores, titulo="Creación de Usuario")
                else:
                    popup_mensaje(ventana, "ingrese nombre y contraseña arriba", fuente_tit, fuente_sub, colores, titulo="Creacion de Usuario", )

        # INPUTS + BOTONES
        dibujar_input(caja_usuario, ventana, config)
        dibujar_input(caja_pass, ventana, config)

        dibujar_boton(boton_login)
        dibujar_boton(boton_registrar)

        pygame.display.update()
        reloj.tick(60)

    return usuario_logueado


# CARGAR IMAGEN
def cargar_imagen(ruta: str, ancho: int | None = None, alto: int | None = None) -> pygame.surface:
    """Carga una imagen desde una ruta y, opcionalmente, la escala.

    Args:
        ruta (str): Ruta completa de la imagen.
        ancho (int | None, optional): Nuevo ancho (opcional).
        alto (int | None, optional): Nuevo alto (opcional).

    Returns:
        pygame.surface | None:
            - La imagen cargada (superficie) si se pudo cargar.
            - None si ocurrió un error.
    """
    imagen = pygame.image.load(ruta).convert_alpha()

    if ancho is not None and alto is not None:
        imagen = pygame.transform.scale(imagen, (ancho, alto))

    return imagen


# DIBUJAR TEXTO
def dibujar_texto(superficie: pygame.surface, texto: str, tamaño: int, color: tuple, x: int, y: int, centro: bool = True, fuente: str = "arial") -> None:
    """Dibuja texto en una superficie.

    Args:
        superficie (pygame.surface): Superficie donde se dibuja el texto.
        texto (str): Texto a renderizar.
        tamaño (int): Tamaño de fuente.
        color (tuple): Color del texto.
        x (int): Posición X.
        y (int): Posición Y.
        centro (bool, optional): Si es True, centra el texto en (x, y). Si es False, usa topleft.
        fuente (str, optional): Nombre de la fuente.

    Returns:
        None
    """
    fuente_obj = pygame.font.SysFont(fuente, tamaño)
    render = fuente_obj.render(texto, True, color)

    rect = render.get_rect()
    if centro:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)

    superficie.blit(render, rect)
