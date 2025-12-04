import os
import json

RUTA_USUARIOS = "/Users/guille/Documents/computacion/wordle/archivos/usuarios.json"

def inicializar_json() -> None:
    """Crea el archivo JSON de usuarios si no existe.

    Returns:
        None
    """
    if not os.path.exists(RUTA_USUARIOS):
        with open(RUTA_USUARIOS, "w") as archivo:
            json.dump({"usuarios": []}, archivo, indent=4)

def cargar_usuarios() -> dict:
    """Lee los datos del archivo usuarios.json.

    Returns:
        dict: Contenido completo del JSON.
    """
    inicializar_json()
    with open(RUTA_USUARIOS, "r") as archivo:
        return json.load(archivo)

def guardar_usuarios(data: dict) -> None:
    """Guarda la información actualizada en usuarios.json.

    Args:
        data (dict): Diccionario con todos los datos que se escribirán.

    Returns:
        None
    """
    with open(RUTA_USUARIOS, "w") as archivo:
        json.dump(data, archivo, indent=4)

def registrar_usuario(nombre: str, contraseña: str) -> None:
    """Registra un nuevo usuario si no existe previamente.

    Args:
        nombre (str): Nombre de usuario.
        contraseña (str): Contraseña elegida por el usuario.

    Returns:
        None
    """
    data = cargar_usuarios()
    existe_usuario = True
    for usuario in data["usuarios"]:
        if usuario["nombre"] == nombre:
            print("⚠️ El usuario ya existe.")
            existe_usuario = False
            break

    if existe_usuario:
        nuevo_usuario = {
            "nombre": nombre,
            "contraseña": contraseña,
            "estadisticas": {
                "puntaje_total": 0,
                "errores": 0,
                "niveles_completados": 0
            }
        }
        data["usuarios"].append(nuevo_usuario)
        guardar_usuarios(data)
        print("✅ Usuario registrado correctamente.")

def login_usuario(nombre: str, contraseña: str) -> dict | None:
    """Valida usuario y contraseña.

    Args:
        nombre (str): Nombre del usuario.
        contraseña (str): Contraseña ingresada.

    Returns:
        dict | None: El diccionario del usuario si es válido, o None si no coincide.
    """
    data = cargar_usuarios()
    resultado = None
    for usuario in data["usuarios"]:
        if usuario["nombre"] == nombre and usuario["contraseña"] == contraseña:
            print(f"👋 Bienvenido {nombre}!")
            resultado = usuario
            break
    if not resultado:
        print("❌ Usuario o contraseña incorrectos.")
    return resultado

def actualizar_estadisticas(nombre: str, puntaje: int, errores: int, nivel: int) -> None:
    """Actualiza las estadísticas acumuladas del usuario.

    Args:
        nombre (str): Nombre del usuario a modificar.
        puntaje (int): Puntos a sumar.
        errores (int): Errores a acumular.
        nivel (int): Último nivel alcanzado.

    Returns:
        None
    """
    data = cargar_usuarios()
    for usuario in data["usuarios"]:
        if usuario["nombre"] == nombre:
            usuario["estadisticas"]["puntaje_total"] += puntaje
            usuario["estadisticas"]["errores"] += errores
            usuario["estadisticas"]["niveles_completados"] = nivel
    guardar_usuarios(data)
    
def inicializar_estadisticas(nombre: str) -> None:
    """Reinicia las estadísticas del usuario a cero.

    Args:
        nombre (str): Usuario cuyas estadísticas se reiniciarán.

    Returns:
        None
    """
    data = cargar_usuarios()
    for usuario in data["usuarios"]:
        if usuario["nombre"] == nombre:
            usuario["estadisticas"]["puntaje_total"] = 0
            usuario["estadisticas"]["errores"] = 0
            usuario["estadisticas"]["niveles_completados"] = 0
    guardar_usuarios(data)
