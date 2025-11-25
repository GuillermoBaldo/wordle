import random
def sistema_comodines(palabra_validada: str, estado_partida: dict, config) -> list[bool]:
    """Gestiona el uso de comodines según la palabra ingresada por el jugador.

    Args:
        palabra_validada (str): Entrada del jugador.
        estado_partida (dict): Información actual de la partida.
        config (_type_): Diccionario con códigos de colores.

    Returns:
        list[bool]: Estado actualizado de las banderas de comodines.
    """
    if palabra_validada == "AYUDA":
        opcion = pedir_opcion_comodin()
        bandera_comodines = estado_partida["bandera_comodines"]
        procesar_opcion_comodin(opcion, bandera_comodines, estado_partida, config)
        return bandera_comodines

    return estado_partida["bandera_comodines"]

def pedir_opcion_comodin() -> str:
    """Muestra el menú de opciones de comodines y devuelve la elección del jugador.

    Returns:
        str: Opción seleccionada por el jugador.
    """
    print("Por cada comodin usado se perderan 20 puntos.")
    print("🔍 1.Revelar letra.")
    print("🔗 2.Revelar Temática.")
    print("🧠 3.Revelar letra desordenada.")
    return input("Ingrese una opción: ")

def procesar_opcion_comodin(opcion: str, bandera_comodines: list[bool], estado_partida: dict, config):
    """Procesa el comodín seleccionado por el jugador.

    Args:
        opcion (str): Comodín elegido.
        bandera_comodines (list[bool]): Control de comodines disponibles.
        estado_partida (dict): Datos de la partida.
        config (_type_): Colores de impresión.
    """
    match opcion:
        case "1":
            usar_comodin_revelar_letra(bandera_comodines, estado_partida, config)
        case "2":
            usar_comodin_tematica(bandera_comodines, estado_partida, config)
        case "3":
            usar_comodin_letra_desordenada(bandera_comodines, estado_partida, config)
        case _:
            print("Opción inválida.")

def usar_comodin_revelar_letra(banderas: list[bool], estado_partida: dict, config: dict) -> None:
    """Revela una letra de la palabra secreta si el comodín está disponible.

    Args:
        banderas (list[bool]): Comodines disponibles.
        estado_partida (dict): Información de la partida.
        config (dict): Código de colores.
    """
    if banderas[0]:
        revelar_letra(estado_partida["secreto"], config)
        estado_partida["comodines_usados"] += 1
        banderas[0] = False
    else:
        print("Comodín ya usado")

def usar_comodin_tematica(banderas: list[bool], estado_partida: dict, config: dict) -> None:
    """Revela la temática de la palabra secreta.

    Args:
        banderas (list[bool]): Control de comodines.
        estado_partida (dict): Datos actuales de la partida.
        config (dict): Colores para mostrar la temática.
    """
    if banderas[1]:
        print(f"{config['GREEN']}{estado_partida['tema']}{config['RESET']}")
        estado_partida["comodines_usados"] += 1
        banderas[1] = False
    else:
        print("Comodín ya usado")

def usar_comodin_letra_desordenada(banderas: list[bool], estado_partida: dict, config: dict) -> None:
    """Muestra una letra aleatoria de la palabra secreta, desordenada.

    Args:
        banderas (list[bool]): Disponibilidad del comodín.
        estado_partida (dict): Información de la partida.
        config (dict): Colores para mostrar la letra.
    """
    if banderas[2]:
        revelar_letra(estado_partida["secreto"], config, True)
        estado_partida["comodines_usados"] += 1
        banderas[2] = False
    else:
        print("Comodín ya usado")



def revelar_letra(secreto: str, config, desorden: bool = False, ) -> str:
	"""Revela una letra del secreto, opcionalmente en una posición aleatoria.

    Args:
        secreto (str): Palabra secreta.
        desorden (bool, optional): Si True, muestra la letra en otra posición. Por efecto, False.

    Returns:
        str: La letra revelada.
	"""

	letra , posicion = letra_aleatoria(secreto)
	if not desorden:
		for i in range (5):
			if i == posicion:
				print(f"{config["GREEN"]}{letra}{config["RESET"]}", end=" ")
			else:
				print(f"{config["GREY"]}X{config["RESET"]}", end=" ")
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

def letra_aleatoria(palabra: str) -> tuple[str, int]:
	"""Devuelve una letra aleatoria de la palabra junto con su índice.

    Args:
        palabra (str): Palabra de origen.

    Returns:
        tuple[str, int]: La letra seleccionada y su posición.
	"""
	indice = random.randrange(len(palabra))
	letra = palabra[indice]
	return letra, indice


