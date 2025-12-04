from manejoJSON import *


def login(nombre: str, contraseña: str) -> dict | None:
    """
    Gestiona el inicio de sesión del usuario desde la interfaz pygame.

    Args:
        nombre (str): nombre de usuario ingresado en pantalla
        contraseña (str): contraseña ingresada en pantalla

    Returns:
        dict | None: datos del usuario si coincide, None si no.
    """

    usuario = None
    if nombre != "" and contraseña != "":
        usuario = login_usuario(nombre, contraseña)

    return usuario



def registrar_nuevo_usuario(nombre: str, contraseña: str) -> dict | None:
    """
    Registra un nuevo usuario cuando se llama desde pygame.

    Args:
        nombre (str): usuario ingresado
        contraseña (str): contraseña ingresada

    Returns:
        dict | None: datos del usuario registrado, None si no se pudo registrar.
    """

    usuario = None

    if nombre != "" and contraseña != "":
        # Guardar al usuario en el JSON
        registrar_usuario(nombre, contraseña)

        # Lo re-leemos del JSON para devolver un dict completo
        usuario = login_usuario(nombre, contraseña)

    return usuario



# ============================================================================
# VERSIONES DE CONSOLA 
# ============================================================================

def login_consola() -> dict | None:
    """
    Mismo login original de consola.
    No se usa en pygame, pero lo dejamos por compatibilidad.
    """
    opcion = input("1.Iniciar sesión\n2.Registrar nuevo usuario\nElige una opción (1-2): ")
    usuario = None
    bandera = True

    while bandera:
        match opcion:
            case "1":
                usuario = iniciar_sesion()
                bandera = False

            case "2":
                usuario = registrar_nuevo_usuario_consola()
                bandera = False

            case _:
                print("Opción inválida. Por favor, elige 1 o 2.")
                opcion = input("1.Iniciar sesión\n2.Registrar nuevo usuario\nElige una opción (1-2): ")

    return usuario



# ============================================================================
# FUNCIONES ORIGINALES AUXILIARES
# ============================================================================

def registrar_nuevo_usuario_consola():
    """
    Versión original por consola.
    """
    print("=== REGISTRO DE USUARIO ===")
    nombre, contraseña = ingreso_datos()
    reingreso = input("Reingresa la contraseña: ")

    while contraseña != reingreso:
        contraseña, reingreso = reingreso_contraseña()

    registrar_usuario(nombre, contraseña)
    usuario = login_usuario(nombre, contraseña)

    return usuario



def iniciar_sesion():
    """
    Versión original por consola.
    """
    print("=== INICIO DE SESIÓN ===")
    nombre, contraseña = ingreso_datos()
    usuario = login_usuario(nombre, contraseña)
    return usuario



def ingreso_datos():
    """
    Función original de consola.
    """
    nombre = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    return nombre, contraseña



def reingreso_contraseña():
    """
    Función original de consola.
    """
    print("Las contraseñas no coinciden. Intenta nuevamente.")
    contraseña = input("Elige una contraseña: ")
    reingreso = input("Reingresa la contraseña: ")
    return contraseña, reingreso
