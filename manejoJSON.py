import os
import json
import re


# =========================
# ARCHIVO: usuarios.json
# =========================/Users/guille/Documents/computacion/UTN/wordel/archivos.py
RUTA_USUARIOS = "/Users/guille/Documents/computacion/wordle/archivos/usuarios.json"

def inicializar_json():
    """Crea el archivo JSON si no existe."""
    if not os.path.exists(RUTA_USUARIOS):
        with open(RUTA_USUARIOS, "w") as archivo:
            json.dump({"usuarios": []}, archivo, indent=4)

def cargar_usuarios():
    """Lee los datos del archivo usuarios.json."""
    inicializar_json()
    with open(RUTA_USUARIOS, "r") as archivo:
        return json.load(archivo)

def guardar_usuarios(data):
    """Guarda la información actualizada en usuarios.json."""
    with open(RUTA_USUARIOS, "w") as archivo:
        json.dump(data, archivo, indent=4)

def registrar_usuario(nombre, contraseña):
    """Registra un nuevo usuario si no existe."""
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

    Returns:
        _str | None_: dict del usuario si es correcto, None si no.
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

def actualizar_estadisticas(nombre, puntaje, errores, nivel):
    """Actualiza las estadísticas de un usuario."""
    data = cargar_usuarios()
    for usuario in data["usuarios"]:
        if usuario["nombre"] == nombre:
            usuario["estadisticas"]["puntaje_total"] += puntaje
            usuario["estadisticas"]["errores"] += errores
            usuario["estadisticas"]["niveles_completados"] = nivel
    guardar_usuarios(data)
    
def inicializar_estadisticas(nombre):
    """Actualiza las estadísticas de un usuario."""
    data = cargar_usuarios()
    for usuario in data["usuarios"]:
        if usuario["nombre"] == nombre:
            usuario["estadisticas"]["puntaje_total"] = 0
            usuario["estadisticas"]["errores"] = 0
            usuario["estadisticas"]["niveles_completados"] = 0
    guardar_usuarios(data)
