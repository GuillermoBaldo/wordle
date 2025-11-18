
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
# palabras=cargar_palabrasv2("/Users/guille/Documents/computacion/wordle/archivos/palabras (1).csv")

# print(palabras)
# for i in range (10):

#     x=elegir_palabra_sin_repetir(palabras)
#     imprimir_diccionario(palabras)
#     print(x[0], x[1])

# palabras=cargar_config("/Users/guille/Documents/computacion/wordle/archivos/config.csv") 
# print(palabras["GREEN"])
# imprimir_diccionario(palabras)

