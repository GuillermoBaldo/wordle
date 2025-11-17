from funciones_espesificas import *
from datos import *
import random

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
	"""_La función muestra el menú principal del juego_

	Returns:
		str: _Opción elegida del jugador_
	"""
	print("=== WORDLE ===")
	print("1) Jugar (palabra aleatoria)")
	print("2) Jugar (introducir palabra secreta)")
	print("3) Instrucciones")
	print("4) Salir")
	choice = input("Elige una opción (1-4): ")
	choice = mi_strip(choice)
	while choice > "4" or choice < "1":
		choice = input("Opción inválida. Elige una opción (1-4): ")
		choice = mi_strip(choice)
	return choice  


def elegir_palabrav2() -> tuple [str, str]:
	"""Elige aleatoriamente una palabra y su tema desde el diccionario PALABRAS_TEMATICAS.

	Returns:
		tuple [str, str]: Una tupla con la palabra seleccionada y el tema correspondiente.
	"""
	tema = random.choice(list(PALABRAS_TEMATICAS.keys()))
	palabra = random.choice(PALABRAS_TEMATICAS[tema])
	palabra = normalizar_palabra(palabra)
	return palabra, tema


def validar_adivinanza(palabra: str) -> str | None:
	"""Valida que la palabra ingresada tenga 5 letras y contenga solo caracteres alfabéticos.

	Args:
		palabra (str): Palabra a validar.

	Returns:
		str | None: La palabra normalizada si es válida, o None si no lo es.
	"""
	palabra = normalizar_palabra(palabra)
	resultado = palabra
	if len(palabra) != 5 or not es_string(palabra):
		resultado = None
	return resultado

def mostrar_feedback(adivinanza: str, secreto: str) -> None:
	"""Muestra por consola un feedback pintado de la adivinanza según la coincidencia con la palabra.

	Args:
		adivinanza (str): Palabra ingresada por el jugador.
		secreto (str): Palabra secreta a adivinar

	Returns:
		None
	"""
	resultado = [""] * 5
	secreto_lista = list(secreto)

	for i in range(5):
		if adivinanza[i] == secreto[i]:
			resultado[i] = f"{GREEN}{adivinanza[i]}{RESET}"
			secreto_lista[i] = None  # se consume la letra

	for i in range(5):
		if resultado[i] != "":
			continue  # ya está verde
		if contiene(secreto_lista, adivinanza[i]):
			resultado[i] = f"{YELLOW}{adivinanza[i]}{RESET}"
			idx = buscar_indice(secreto_lista, adivinanza[i])
			secreto_lista[idx] = None
		else:
			resultado[i] = f"{GRAY}{adivinanza[i]}{RESET}"

	mostrar_lista_colores(resultado)


def jugar(nivel, partida, vidas, puntos, comodines_usados, secreto=None):
	secreto , tema, intentos, errores, ganaste, bandera_comodines = configurar_partida(secreto)
	ganaste, intentos, errores, comodines_usados=jugar_partida(nivel, partida, vidas, puntos, intentos, errores, tema , bandera_comodines , comodines_usados ,secreto)
	if not ganaste:
		print(f"Se acabaron los intentos. La palabra era: {RED}{secreto}{RESET}\n")
	return ganaste , intentos , errores , comodines_usados

def jugar_secreto(nivel, partida , vidas, puntaje):
	secreto = input("Introduce la palabra secreta (5 letras, no se mostrará): ")
	secreto = normalizar_palabra(secreto)
	if validar_input(validar_adivinanza(secreto), None):
		jugar(nivel, partida , vidas, puntaje ,secreto)


def letra_aleatoria(palabra):
    indice = random.randrange(len(palabra))
    letra = palabra[indice]
    return letra, indice

def revelar_letra(secreto , desorden=False):
	letra , posicion = letra_aleatoria(secreto)
	if not desorden:
		for i in range (5):
			if i == posicion:
				print(f"{GREEN}{letra}{RESET}", end=" ")
			else:
				print(f"{GRAY}X{RESET}", end=" ")
		print()
	else:
		posicion_aleatoria = random.randint(1, 5)
		while posicion == posicion_aleatoria:
			posicion_aleatoria = random.randint(1, 5)
		for i in range (5):
			if i == posicion_aleatoria:
				print(f"{YELLOW}{letra}{RESET}", end=" ")
			else:
				print(f"{GRAY}X{RESET}", end=" ")
		print()
	return letra

def sistema_comodines(palabra_validada, secreto, tema, bandera_comodines, comodines_usados):
	if palabra_validada == "AYUDA":
		opcion = input("Por cada comodin usado se perderan 20 puntos.\n🔍 1.Revelar letra. \n🔗 2.Revelar Temática. \n🧠 3.Revelar letra desordenada. \nIngrese una opcion: ")
		match opcion:
			case "1":
				if bandera_comodines[0]:
					revelar_letra(secreto)
					comodines_usados += 1
					bandera_comodines[0] = False
				else:
					print("comodin ya usado")
			case "2":
				if bandera_comodines[1]:
					print(f"{GREEN}{tema}{RESET}")
					comodines_usados += 1
					bandera_comodines[1] = False
				else:
					print("comodin ya usado")
			case "3":
				if bandera_comodines[2]:
					revelar_letra(secreto, True)
					comodines_usados += 1
					bandera_comodines[2] = False
				else:
					print("comodin ya usado")
			case _:
				print("opcion invalida.")
	return bandera_comodines, comodines_usados

def jugar_partida(nivel, partida, vidas, puntos, intentos, errores, tema , bandera_comodines , comodines_usados,secreto):
	ganaste = False
	while intentos <= MAX_ATTEMPTS:
		print(f"Nivel {nivel} | Partida {partida} | Vidas {vidas} | Puntos {puntos}")
		palabra = input(f"Intento {intentos}/{MAX_ATTEMPTS}: ")
		palabra = normalizar_palabra(palabra)
		palabra_validada = validar_adivinanza(palabra)
		

		if not palabra_validada:
			print("Entrada inválida. Introduce exactamente 5 letras.")
			continue

		bandera_comodines, comodines_usados = sistema_comodines(palabra_validada, secreto, tema, bandera_comodines, comodines_usados)

		if palabra_validada == secreto:
			print(f"¡Felicidades! Adivinaste la palabra en {GREEN}{intentos}{RESET} intentos.\n")
			ganaste = True
			break
		elif palabra_validada != secreto and palabra_validada != "AYUDA":
			mostrar_feedback(palabra_validada, secreto)
			intentos += 1
			errores +=1
	return ganaste , intentos , errores , comodines_usados

def configurar_partida(secreto):
	if secreto == None:
		secreto, tema = elegir_palabrav2()
	else:
		secreto = normalizar_palabra(secreto)
	intentos = 1
	errores=0
	print(f"\nTienes {GREEN}{MAX_ATTEMPTS}{RESET} intentos para adivinar una palabra de 5 letras.")
	print(f'Ingrese la palabra "{GREEN}ayuda{RESET}" para poder acceder a los comodines ')
	ganaste = False
	bandera_comodines = [True, True, True]
	return secreto , tema, intentos, errores, ganaste, bandera_comodines