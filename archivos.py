import os
import json
import re

# =========================
# ARCHIVO: usuarios.json
# =========================/Users/guille/Documents/computacion/UTN/wordel/archivos.py
RUTA_USUARIOS = "/Users/guille/Documents/computacion/UTN/wordel/usuarios.json"

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
    for usuario in data["usuarios"]:
        if usuario["nombre"] == nombre:
            print("⚠️ El usuario ya existe.")
            return False
    
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
    return True

def login_usuario(nombre, contraseña):
    """Valida usuario y contraseña."""
    data = cargar_usuarios()
    for usuario in data["usuarios"]:
        if usuario["nombre"] == nombre and usuario["contraseña"] == contraseña:
            print(f"👋 Bienvenido {nombre}!")
            return usuario
    print("❌ Usuario o contraseña incorrectos.")
    return None

def actualizar_estadisticas(nombre, puntaje, errores, nivel):
    """Actualiza las estadísticas de un usuario."""
    data = cargar_usuarios()
    for usuario in data["usuarios"]:
        if usuario["nombre"] == nombre:
            usuario["estadisticas"]["puntaje_total"] += puntaje
            usuario["estadisticas"]["errores"] += errores
            usuario["estadisticas"]["niveles_completados"] = nivel
    guardar_usuarios(data)

# =========================
# ARCHIVO: partidas.csv
# =========================
RUTA_PARTIDAS = "/Users/guille/Documents/computacion/UTN/wordel/partidas.csv"

def inicializar_csv():
    """Crea el archivo CSV si no existe."""
    if not os.path.exists(RUTA_PARTIDAS):
        with open(RUTA_PARTIDAS, "w") as archivo:
            archivo.write("nombre,nivel,partida,palabra,resultado,puntaje,errores\n")

def guardar_partida(nombre, nivel, partida, palabra, resultado, puntaje, errores):
    """Guarda los datos de una partida en el CSV."""
    inicializar_csv()
    linea = f"{nombre},{nivel},{partida},{palabra},{resultado},{puntaje},{errores}\n"
    with open(RUTA_PARTIDAS, "a") as archivo:
        archivo.write(linea)

def parser_csv(path) -> list:
    """
    Lee el CSV con regex y devuelve una lista de diccionarios.
    Usa el mismo formato del ejemplo dado por el usuario.
    """
    lista_partidas = []

    if not os.path.exists(path):
        print(f"⚠️ El archivo {path} no existe.")
        return lista_partidas

    with open(path, "r") as archivo:
        encabezado = True
        for linea in archivo:
            if encabezado:
                encabezado = False
                continue
            dicionario = {}
            lista = re.split(",|\n", linea.strip())
            if len(lista) >= 7:
                dicionario["nombre"] = lista[0]
                dicionario["nivel"] = lista[1]
                dicionario["partida"] = lista[2]
                dicionario["palabra"] = lista[3]
                dicionario["resultado"] = lista[4]
                dicionario["puntaje"] = lista[5]
                dicionario["errores"] = lista[6]
                lista_partidas.append(dicionario)

    return lista_partidas
