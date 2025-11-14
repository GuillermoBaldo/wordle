PALABRAS_TEMATICAS = {
    "animales": ["tigre","cebra","raton","zorro","burro"],
    "paises": ["chile","china","india","haiti","japon"],
    "tecnologia": ["robot","cable","clave","tecla","laser"],
    "naturaleza": ["barro","hojas","llano","arena","monte"],
    "comida": ["pizza","arroz ","fruta","leche","salsa"],
    "objetos": ["silla","plato","libro","lapiz","radio"]
}
# ANSI colors

GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RED = "\033[91m"
RESET = "\033[0m"

MAX_ATTEMPTS = 6
from manejoCSV import *
def imprimir_diccionario(dicc):
    """
    Imprime un diccionario de forma estética.
    Sin comprensiones de lista.
    """
    print("\n========== DICCIONARIO ==========\n")

    for clave in dicc:
        valor = dicc[clave]

        # Si es una lista (como palabras por categoría)
        if isinstance(valor, list):
            print(f"{clave}:")
            i = 0
            while i < len(valor):
                print(f"   - {valor[i]}")
                i += 1
        else:
            # Si es un valor simple
            print(f"{clave}: {valor}")

    print("\n=================================\n")
palabras=cargar_palabras("/Users/guille/Documents/computacion/wordle/archivos/palabras.csv")
for i in range (10):

    x=elegir_palabra_sin_repetir(palabras)
    imprimir_diccionario(palabras)
    print(x)