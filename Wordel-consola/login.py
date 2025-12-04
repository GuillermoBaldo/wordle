from manejoJSON import *
from mostrar_datos import *


def login() -> dict | None:
    """Gestiona el registro o inicio de sesión del usuario.
    Si es su primera vez, lo registra. Si ya existe, se valida su usuario y contraseña.

    Returns:
        dict | None: Diccionario con los datos del usuario si el login es exitoso, o None si las credenciales no corresponden.
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
                usuario = registrar_nuevo_usuario()
                bandera = False
            case _:
                print("Opción inválida. Por favor, elige 1 o 2.")
                opcion = input("1.Iniciar sesión\n2.Registrar nuevo usuario\nElige una opción (1-2): ")
    return usuario

def registrar_nuevo_usuario():
    """Función auxiliar para registrar un nuevo usuario desde la consola."""
    print("=== REGISTRO DE USUARIO ===")
    nombre, contraseña = ingreso_datos()
    reingreso = input("Reingresa la contraseña: ")
    
    while contraseña != reingreso:
        contraseña, reingreso = reingreso_contraseña()
    
    registrar_usuario(nombre, contraseña)
    usuario = login_usuario(nombre, contraseña)
    
    return usuario

def iniciar_sesion():
    """Función auxiliar para iniciar sesión desde la consola."""
    print("=== INICIO DE SESIÓN ===")
    nombre, contraseña = ingreso_datos()
    usuario = login_usuario(nombre, contraseña)
    return usuario

def ingreso_datos():
    """Solicita al usuario ingresar su nombre de usuario y contraseña desde la consola.

    Returns:
        tuple: Tupla que contiene el nombre de usuario y la contraseña ingresados.
    """
    nombre = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    return nombre, contraseña

def reingreso_contraseña():
    """Solicita al usuario reingresar su contraseña para confirmación.

    Returns:
        str: Contraseña reingresada por el usuario.
    """
    print("Las contraseñas no coinciden. Intenta nuevamente.")
    contraseña = input("Elige una contraseña: ")
    reingreso = input("Reingresa la contraseña: ")
    return contraseña, reingreso