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
	print("2) Instrucciones")
	print("3) Salir")
	choice = input("Elige una opción (1-3): ")
	choice = mi_strip(choice)
	while choice > "3" or choice < "1":
		choice = input("Opción inválida. Elige una opción (1-3): ")
		choice = mi_strip(choice)
	return choice 

def importar_configuracion(ruta):
    estado_jugador = cargar_config(ruta)
    return estado_jugador

def validar_adivinanza(palabra: str) -> str | None:
	palabra = normalizar_palabra(palabra)
	resultado = palabra
	if len(palabra) != 5 or not es_string(palabra):
		resultado = None
	return resultado

def mostrar_feedback(adivinanza, secreto):
    config = importar_configuracion("/Users/guille/Documents/computacion/wordle/archivos/config.csv")

    # Colores que vienen del archivo config.csv
    green = config["GREEN"]
    yellow = config["YELLOW"]
    gray = config["GRAY"]
    reset = config["RESET"]

    resultado = [""] * 5
    secreto_lista = list(secreto)

    # Primera pasada: letras correctas (verde)
    for i in range(5):
        if adivinanza[i] == secreto[i]:
            resultado[i] = f"{green}{adivinanza[i]}{reset}"
            secreto_lista[i] = None  # Consumir letra

    # Segunda pasada: letra existe pero mal ubicada (amarillo)
    for i in range(5):
        if resultado[i] != "":
            continue  # ya está verde
        if contiene(secreto_lista, adivinanza[i]):
            resultado[i] = f"{yellow}{adivinanza[i]}{reset}"
            idx = buscar_indice(secreto_lista, adivinanza[i])
            secreto_lista[idx] = None
        else:
            resultado[i] = f"{gray}{adivinanza[i]}{reset}"

    mostrar_lista_colores(resultado)



def jugar(estado_partida, palabras):
	config = importar_configuracion("/Users/guille/Documents/computacion/wordle/archivos/config.csv")
	configurar_partida(estado_partida, palabras,) 
	jugar_partida(estado_partida)
	if not estado_partida["ganaste"]:
		print(f"Se acabaron los intentos. La palabra era: {config["RED"]}{estado_partida["secreto"]}{config["RESET"]}\n")
	

def letra_aleatoria(palabra):
    indice = random.randrange(len(palabra))
    letra = palabra[indice]
    return letra, indice

def revelar_letra(secreto , desorden=False):
	config = importar_configuracion("/Users/guille/Documents/computacion/wordle/archivos/config.csv")
	letra , posicion = letra_aleatoria(secreto)
	if not desorden:
		for i in range (5):
			if i == posicion:
				print(f"{config["GREEN"]}{letra}{config["RESET"]}", end=" ")
			else:
				print(f"{config["GRAY"]}X{config["RESET"]}", end=" ")
		print()
	else:
		posicion_aleatoria = random.randint(1, 5)
		while posicion == posicion_aleatoria:
			posicion_aleatoria = random.randint(1, 5)
		for i in range (5):
			if i == posicion_aleatoria:
				print(f"{config["YELLOW"]}{letra}{config["RESET"]}", end=" ")
			else:
				print(f"{config["GREY"]}X{config["RESET"]}", end=" ")
		print()
	return letra

def sistema_comodines(palabra_validada, estado_partida):
	config = importar_configuracion("/Users/guille/Documents/computacion/wordle/archivos/config.csv")
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
						print(f"{config["GREEN"]}{estado_partida["tema"]}{config["RESET"]}")
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
	config = importar_configuracion("/Users/guille/Documents/computacion/wordle/archivos/config.csv")
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
			print(f"¡Felicidades! Adivinaste la palabra en {config["GREEN"]}{estado_partida["intentos"]}{config["RESET"]} intentos.\n")
			estado_partida["ganaste"] = True
			break
		elif palabra_validada != estado_partida["secreto"] and palabra_validada != "AYUDA":
			mostrar_feedback(palabra_validada, estado_partida["secreto"])
			estado_partida["intentos"] += 1
			estado_partida["errores"] +=1
	return estado_partida["ganaste"]

def configurar_partida(estado_partida,palabras):

	palabras_elegidas = elegir_palabra_sin_repetir(palabras)
	estado_partida["tema"] = palabras_elegidas[1]
	estado_partida["secreto"] = normalizar_palabra(palabras_elegidas[0])

	print(estado_partida["secreto"])
	estado_partida["intentos"] = 1
	estado_partida["errores"] = 0
	estado_partida["comodines_usados"] = 0
	estado_partida["ganaste"] = False
	estado_partida["bandera_comodines"] = [True, True, True]