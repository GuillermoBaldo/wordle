from funciones_espesificas import *
from manejoCSV import *


def mostrar_instrucciones_juego():

    instrucciones = """
⭐ Instrucciones del Juego ⭐

## 🎮 Desarrollo del Juego
---
El juego se compone de **5 niveles**, y cada nivel contiene **3 partidas**.

### ⚙️ Mecánicas por Nivel:
* Se te indicará en qué nivel te encuentras.
* **Pérdida de Vida:** Cada vez que pierdas una partida, **pierdes una vida**.
* **Reinicio de Nivel:** Si pierdes las **3 vidas**, el nivel se **reinicia**.

### 📊 Resumen de Progreso:
Al finalizar un nivel, se mostrará un resumen de tu progreso, que incluye:
* Puntaje acumulado
* Cantidad de errores cometidos
* Cantidad de vidas restantes

## 💡 Comodines (Uso Único)
---
Durante la partida, dispones de **3 comodines** de uso único, que puedes activar en cualquier momento de la partida:

1.  **🔍 Revelar letra:** Muestra una letra válida en su respectiva posición.
2.  **🔗 Temática:** Muestra una temática relacionada con la palabra a revelar.
3.  **🧠 Comodín extra:** Muestra una letra en una posición incorrecta.

## 🏆 Final del Juego
---
* **Victoria:** Si logras completar los **5 niveles**, el juego mostrará un **mensaje de victoria** junto con tus estadísticas finales (puntaje total, errores, tiempo, etc.).
* **Derrota:** En caso contrario (agotar los reinicios o no completar los 5 niveles), se informará la derrota y finalizará el juego.
"""
    print(instrucciones)

def mostrar_menu()->str:
	"""Muestra el menú principal del juego y solicita una opción al usuario.

    Returns:
        str: Opción ingresada por el jugador, validada entre '1' y '3'.
	"""
	print("=== WORDLE ===")
	print("1) Jugar (palabra aleatoria)\n2) Instrucciones\n3) Salir")
	choice = input("Elige una opción (1-3): ")
	choice = mi_strip(choice)
	while choice > "3" or choice < "1":
		choice = input("Opción inválida. Elige una opción (1-3): ")
		choice = mi_strip(choice)
	return choice 

def validar_adivinanza(palabra: str) -> str | None:
	"""Valida que la palabra ingresada sea un string de 5 letras.

    Args:
        palabra (str): Palabra ingresada por el usuario.

    Returns:
        str | None: La palabra normalizada si es válida, o None si no cumple las condiciones.
	"""
	palabra = normalizar_palabra(palabra)
	resultado = palabra
	if len(palabra) != 5 or not es_string(palabra):
		resultado = None
	return resultado

def mostrar_lista_colores(lista):
    """Imprime en pantalla todos los elementos de una lista, separados por espacios.

    Args:
        lista (list): Lista a mostrar.
    """
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()


def mostrar_feedback(adivinanza: str, secreto: str, config: dict) -> None:
    """Genera y muestra el feedback visual de colores del intento del jugador.

    Args:
        adivinanza (str): Palabra ingresada por el jugador.
        secreto (str): Palabra secreta a divinar.
        config (dict): Diccionario con los códigos de colores.
    """
    estado = {
		"adivinanza": adivinanza,
		"secreto": secreto,
		"config": config,
		"resultado": [""] * 5,
		"secreto_lista": list(secreto)
	}

    marcar_coincidencias_exactas(estado)
    marcar_coincidencias_parciales(estado)
    mostrar_lista_colores( estado["resultado"])

def marcar_coincidencias_exactas(estado: dict) -> None:
    """Marca las letras correctas en la posición correcta en verde.

    Args:
        estado (dict): Diccionario con la información del intento.
    """
    for i in range(5):
        if estado["adivinanza"][i] == estado["secreto"][i]:
            letra = estado["adivinanza"][i]
            estado["resultado"][i] = (
                f"{estado['config']['GREEN']}{letra}{estado['config']['RESET']}"
            )
            estado["secreto_lista"][i] = None

def marcar_coincidencias_parciales(estado: dict) -> None:
    """Marca letras correctas en posiciones incorrectas en amarillo y letras incorrectas en gris.

    Args:
        estado (dict): Diccionario con datos del intento y progreso.
    """
    for i in range(5):
        if estado["resultado"][i] != "":
            continue

        letra = estado["adivinanza"][i]

        if letra in estado["secreto_lista"]:
            idx = estado["secreto_lista"].index(letra)
            estado["secreto_lista"][idx] = None
            estado["resultado"][i] = (
                f"{estado['config']['YELLOW']}{letra}{estado['config']['RESET']}"
            )
        else:
            estado["resultado"][i] = (
                f"{estado['config']['GREY']}{letra}{estado['config']['RESET']}"
            )

