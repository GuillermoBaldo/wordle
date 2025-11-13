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


def elegir_palabrav2():
    tema = random.choice(list(PALABRAS_TEMATICAS.keys()))
    palabra = random.choice(PALABRAS_TEMATICAS[tema])
    palabra = normalizar_palabra(palabra)
    return palabra, tema

def validar_adivinanza(palabra: str) -> str | None:
	palabra = normalizar_palabra(palabra)
	resultado = palabra
	if len(palabra) != 5 or not es_string(palabra):
		resultado = None
	return resultado

def mostrar_feedback(adivinanza, secreto):
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


def jugar(estado_partida):
	configurar_partida(estado_partida, estado_partida["secreto"]) 
	#ganaste, intentos, errores, comodines_usados=jugar_partida(nivel, partida, vidas, puntos, intentos, errores, tema , bandera_comodines , comodines_usados ,secreto)
	ganaste=jugar_partida(estado_partida)
	if not ganaste:
		print(f"Se acabaron los intentos. La palabra era: {RED}{estado_partida["secreto"]}{RESET}\n")
	

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

def sistema_comodines(palabra_validada, estado_partida):
	if palabra_validada == "AYUDA":
		opcion = input("Por cada comodin usado se perderan 20 puntos.\n🔍 1.Revelar letra. \n🔗 2.Revelar Temática. \n🧠 3.Revelar letra desordenada. \nIngrese una opcion: ")
		bandera_comodines = estado_partida["bandera_comodines"]	
		match opcion:
				case "1":
					if bandera_comodines[0]:
						revelar_letra(estado_partida["secreto"])
						estado_partida["comodines_usados"] += 1
						bandera_comodines[0] = False
					else:
						print("comodin ya usado")
				case "2":
					if bandera_comodines[1]:
						print(f"{GREEN}{estado_partida["tema"]}{RESET}")
						estado_partida["comodines_usados"] += 1
						bandera_comodines[1] = False
					else:
						print("comodin ya usado")
				case "3":
					if bandera_comodines[2]:
						revelar_letra(estado_partida["secreto"], True)
						estado_partida["comodines_usados"] += 1
						bandera_comodines[2] = False
					else:
						print("comodin ya usado")
				case _:
					print("opcion invalida.")
		return bandera_comodines

def jugar_partida(estado_partida):
	while estado_partida["intentos"] <= MAX_ATTEMPTS:
		print(f"Nivel {estado_partida["nivel"]} | Partida {estado_partida["partida"]} | Vidas {estado_partida["vidas"]} | Puntos {estado_partida["puntaje"]}")
		palabra = input(f"Intento {estado_partida["intentos"]}/{MAX_ATTEMPTS}: ")
		palabra = normalizar_palabra(palabra)
		palabra_validada = validar_adivinanza(palabra)
		

		if not palabra_validada:
			print("Entrada inválida. Introduce exactamente 5 letras.")
			continue

		sistema_comodines(palabra_validada, estado_partida)

		if palabra_validada == estado_partida["secreto"]:
			mostrar_feedback(palabra_validada, estado_partida["secreto"])
			print(f"¡Felicidades! Adivinaste la palabra en {GREEN}{estado_partida["intentos"]}{RESET} intentos.\n")
			estado_partida["ganaste"] = True
			break
		elif palabra_validada != estado_partida["secreto"] and palabra_validada != "AYUDA":
			mostrar_feedback(palabra_validada, estado_partida["secreto"])
			estado_partida["intentos"] += 1
			estado_partida["errores"] +=1
	return estado_partida["ganaste"]

def configurar_partida(estado_partida, secreto):
	secreto = None
	if secreto is None:
		secreto, tema = elegir_palabrav2()
		estado_partida["tema"] = tema
	print(secreto)
	estado_partida["intentos"] = 1
	estado_partida["errores"] = 0
	estado_partida["comodines_usados"] = 0
	estado_partida["secreto"] = secreto
	estado_partida["ganaste"] = False
	estado_partida["bandera_comodines"] = [True, True, True]