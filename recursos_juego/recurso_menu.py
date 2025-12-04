import pygame
import sys
import time
from manejoCSV import *
from recursos_juego.boton import crear_boton, dibujar_boton, boton_fue_presionado
from pantallas.pantalla_jugar import *
from manejoJSON import *
from logica_juego import *
from pantallas.pantalla_instrucciones import pantalla_instrucciones
from pantallas.pantalla_estadisticas import pantalla_estadisticas

def cargar_recursos_menu(config: dict) -> dict:
    """Carga todos los recursos del menú principal y devuelve un diccionario."""
    
    recursos = {
        "sonido_click": pygame.mixer.Sound(config["sonido"]["CLICK"]),
        "fondo": pygame.image.load("imagenes/Menu wordle.jpg").convert(),

        "volumen_on": pygame.transform.scale(
            pygame.image.load("imagenes/volumen on.png").convert_alpha(), (85, 85)
        ),

        "volumen_off": pygame.transform.scale(
            pygame.image.load("imagenes/volumen off.png").convert_alpha(), (85, 85)
        ),

        "fuente_tit": pygame.font.SysFont(*config["FUENTES"]["TITULO"]),
        "fuente_sub": pygame.font.SysFont(*config["FUENTES"]["SUBTITULO"]),
    }

    recursos["sonido_click"].set_volume(0.5)

    return recursos



def crear_botones_menu(ventana, config):
    """Crea y posiciona los tres botones del menú principal:
    'Nueva Partida', 'Instrucciones' y 'Estadísticas'.

    Args:
        ventana (pygame.surface): Ventana donde se dibujarán los botones.
        config (dict): Configuración general del juego, usada para obtener las dimensiones y fuentes, entre otros datos.

    Returns:
        tuple:
            - btn_jugar (dict): Botón para iniciar una nueva partida.
            - btn_instr (dict): Botón para abrir instrucciones.
            - btn_stats (dict): Botón para ver estadísticas del usuario.
    """
    x = config["ANCHO"] // 2 - 300 // 2
    y_inicial = 240
    espacio = 20
    ancho, alto = 300, 60

    btn_jugar = crear_boton(ventana, (ancho, alto), (x, y_inicial), texto="Nueva Partida")
    btn_instr = crear_boton(ventana, (ancho, alto), (x, y_inicial + alto + espacio), texto="Instrucciones")
    btn_stats = crear_boton(ventana, (ancho, alto), (x, y_inicial + 2 * (alto + espacio)), texto="Estadísticas")

    return btn_jugar, btn_instr, btn_stats


def manejar_click_boton_sonido(evento, estado, recursos):
    """Controla el botón de sonido (ON/OFF) del menú.
    Cambia el estado de muteo y devuelve el icono correspondiente.

    Args:
        evento (pygame.event.Event): Evento del mouse.
        rect_volumen (pygame.Rect): Área clickeable del icono de volumen.
        muteado (bool): Estado actual del audio (True = muteado).
        volumen_on (pygame.surface): Imagen del icono de volumen activado.
        volumen_off (pygame.surface): Imagen del icono de volumen desactivado.

    Returns:
        tuple:
            - muteado (bool): Nuevo estado del volumen después del clic.
            - icono (pygame.surface | None):
                El icono que debe mostrarse (ON/OFF) o None si no se tocó el botón.

    """

    rect_volumen = estado["rect_volumen"]

    if rect_volumen.collidepoint(evento.pos):
        # Cambiar el estado de muteado
        estado["muteado"] = not estado["muteado"]

        if estado["muteado"]:
            pygame.mixer.music.set_volume(0)
            estado["icono_volumen"] = recursos["volumen_off"]
        else:
            pygame.mixer.music.set_volume(0.5)
            estado["icono_volumen"] = recursos["volumen_on"]



def ejecutar_jugar(config, usuario, recursos, ventana):
    """  Inicia el flujo principal de juego: carga palabras, ejecuta niveles, mide tiempo total jugado y actualiza estadísticas del usuario.

    Args:
        config (dict): Configuración general del juego (tamaños, rutas, colores, etc).
        usuario (dict): Datos del usuario logueado (nombre, contraseña, estadísticas).
        sonido_click (pygame.mixer.Sound): Sonido de clic para los botones.
        ventana (pygame.surface): Ventana principal donde se dibuja el juego.
    """
    recursos["sonido_click"].play()
    palabras = cargar_palabrasv2("archivos/palabras (1).csv")

    inicio = time.time()

    inicializar_estadisticas(usuario["nombre"])
    jugar_niveles(palabras, config, ventana, usuario)

    fin = time.time()
    total_segundos = fin - inicio

    actualizar_estadistica_tiempo(usuario["nombre"], total_segundos)
    usuario = login_usuario(usuario["nombre"], usuario["contraseña"])

    pantalla_estadisticas(ventana, config, usuario["estadisticas"])


def ejecutar_instrucciones(config, ventana, recursos):
    """Ejecuta la pantalla de instrucciones del juego.

    Args:
        config (dict): Configuración del juego.
        ventana (pygame.surface): Ventana donde se dibujan las instrucciones.
        sonido_click (pygame.mixer.Sound): Sonido al presionar el botón.
    """
    recursos["sonido_click"].play()
    pantalla_instrucciones(ventana, config)


def ejecutar_estadisticas(config, ventana, usuario, recursos):
    """Muestra la pantalla de estadísticas del usuario.

    Args:
        config (dict): Configuración general del juego.
        ventana (pygame.surface): Ventana donde se dibuja la pantalla.
        usuario (dict): Usuario actualmente logueado.
        sonido_click (pygame.mixer.Sound): Sonido al presionar un botón.
    """
    recursos["sonido_click"].play()
    usuario = login_usuario(usuario["nombre"], usuario["contraseña"])
    pantalla_estadisticas(ventana, config, usuario["estadisticas"])


def dibujar_menu(ventana, config, usuario, recursos, estado):
    
    ventana.blit(recursos["fondo"], (0, 0))
    ventana.blit(estado["icono_volumen"], estado["rect_volumen"])

    texto = recursos["fuente_tit"].render(
        f"Bienvenid@ {usuario['nombre']}!", True, (179, 0, 134)
    )
    ventana.blit(texto, (config["ANCHO"] // 2 - texto.get_width() // 2, 120))

    subt = recursos["fuente_sub"].render(
        "Seleccioná una opción para empezar :3",
        True, (179, 0, 134)
    )
    ventana.blit(subt, (config["ANCHO"] // 2 - subt.get_width() // 2, 160))

    dibujar_botones(estado["botones"])

def crear_estado_menu(ventana, config, recursos):
    """Inicializa y devuelve el estado completo del menú principal."""

    estado = {
        "muteado": False,
        "icono_volumen": recursos["volumen_on"],
        "rect_volumen": recursos["volumen_on"].get_rect(topleft=(5, 5)),
        "botones": list(crear_botones_menu(ventana, config))
    }

    return estado