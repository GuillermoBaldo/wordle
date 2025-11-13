# mi_slicing 
def rebanar(cadena: str, inicio: int, finalizacion: int, reverse: bool = False  ) -> str:
    """Devuelve una subcadena de 'cadena' entre las posiciones 'inicio' y 'finalizacion'

    Args:
        cadena (str): cadena original de la cual se extenderá una parte
        inicio (int): índice inicial desde donde comenzar a copiar
        finalizacion (int): índica final (no incluído) hasta donde copiar
        reverse (bool, optional): indica si la subcadena debe devolverse invertida. Por defecto es False.

    Returns:
        str: La subcadena obtenida según los parámetros indicados
    """
    cadena_auxiliar = ""
    if not reverse :
        for caracter in range(inicio, finalizacion):
            cadena_auxiliar += cadena[caracter]
            # print(cadena[caracter], end="")
    else:
        for caracter in range(finalizacion-1, inicio-1, -1):
            cadena_auxiliar += cadena[caracter]
    return cadena_auxiliar

def invertir_letra(letra:str, es_minucula: bool=True) -> str:
    """Convierte una letra de minúscula a mayúscula según el valor del parámetro

    Args:
        letra (str): letra a convertir
        es_minucula (bool, optional): True: convierte de minúscula a mayúscula. False: convierte de mayúscula a minúscula. Por defecto es True

    Returns:
        str: Letra convertida
    """
    if es_minucula:
        resultado = chr(ord(letra) - 32)
    else:
        resultado = chr(ord(letra) + 32)
    return resultado

def Mi_Upper(cadena: str) -> str:
    """Convierte todas las letras minúsculas de una cadena en mayúsculas

    Args:
        cadena (str): Cadena de texto a convertir

    Returns:
        str: Cadena en mayúscula
    """
    cadena_mayuscula = ""
    for letra in range(len(cadena)):
        caracter = cadena[letra]
        letra_mayuscula = caracter
        if caracter >= "a" and caracter <= "z":  # si el caracter está entre 'a' y 'z'
            letra_mayuscula = invertir_letra(caracter)
        cadena_mayuscula += letra_mayuscula
    return cadena_mayuscula

def Mi_Lower(cadena: str) -> str:
    """Convierte todas las letras mayúsculas de una cadena en minúsculas

    Args:
        cadena (str): Cadena de texto a convertir

    Returns:
        str: Cadena en minúscula
    """
    cadena_minuscula = ""
    for letra in range(len(cadena)):
        caracter = cadena[letra]
        letra_minuscula = caracter
        if caracter >= "A" and caracter <= "Z":  # si el caracter está entre 'a' y 'z'
            letra_minuscula = invertir_letra(caracter, False)
        cadena_minuscula += letra_minuscula
    return cadena_minuscula

def Mi_capitalize(cadena: str) -> str:
    """Convierte la primera letra a mayúscula y el resto a minúscula

    Args:
        cadena (str): Cadena de texto a convertir

    Returns:
        str: Cadena con la primera letra en mayúscula y las demás en minúscula
    """
    cadena_capitalize= ""
    for letra in range (len(cadena)):
        caracter = cadena[letra]
        letra_cambiada = caracter
        if (caracter >= "A" and caracter <= "Z") or (caracter >= "a" and caracter <= "z"):
            if letra == 0 and (caracter >= "a" and caracter <= "z"):
                letra_cambiada = invertir_letra(caracter)
            elif caracter >= "A" and caracter <= "Z":
                letra_cambiada = invertir_letra(caracter, False)
        cadena_capitalize += letra_cambiada
    return cadena_capitalize

def mi_strip(texto: str, caracter: str = " ") -> str:
    """Elimina los espacios al inicio y al final de la cadena

    Args:
        texto (str): Texto a procesar
        caracter (str, optional): Espacio a eliminar

    Returns:
        str: Texto sin los espacios de los extremos
    """
    inicio = 0
    fin = len(texto) - 1
    while inicio <= fin and texto[inicio] == caracter:
        inicio += 1

    while fin >= inicio and texto[fin] == caracter:
        fin -= 1

    resultado = texto[inicio:fin+1]
    return resultado

def es_string(cadena: str) -> bool:
    """Verifica si una cadena contiene únicamente letras y espacios

    Args:
        cadena (str): Cadena a verificar

    Returns:
        bool: True: cadena solo con letras o espacios. Sino, False
    """
    resultado= True
    for letra in range (len(cadena)):
        caracter = cadena[letra]
        if not ((caracter >= "A" and caracter <= "Z") or (caracter >= "a" and caracter <= "z") or caracter == " "):
            resultado= False
    return resultado

def es_int(cadena: str) -> bool:
    """Verifica si una cadena representa un número válido

    Args:
        cadena (str): Cadena a verificar

    Returns:
        bool: True: cadena solo con dígitos. Sino, False
    """
    resultado= True
    for letra in range (len(cadena)):
        caracter = cadena[letra]
        if not (caracter >= "0" and caracter <= "9" or caracter== ".") :
            resultado= False
    return resultado


def validar_letra(letra:str )-> tuple[bool, str]:
    """Valida que el valor ingresado sea una sola letra del alfabeto

    Args:
        letra (str): Valor a validar

    Returns:
        tuple[bool, str]: Una tupla con un booleano indicando si es válido y la letra en minúscula
    """
    # valida que el ingreso sea una letra
    resultado = False
    if len(letra) == 1 and  es_string(letra):
        letra = Mi_Lower(letra)        
        resultado = True
    return resultado, letra

def buscar_indice(lista: list, elemento: any) -> int:
    """Devuelve el índice de la primera aparición del elemento o -1 si no está

    Args:
        lista (list): Lista donde buscar
        elemento (any): Elemento a buscar

    Returns:
        int: Índice del elemento si se encuentra, -1 en caso contrario
    """
    indice = -1
    for i in range(len(lista)):
        if lista[i] == elemento and indice == -1:
            indice = i
    return indice

def contiene(lista: list, elemento: any) -> bool:
    """Devuelve True si el elemento está en la lista.

    Args:
        lista (list): Lista donde buscar
        elemento (any): Elemento a verificar

    Returns:
        bool: True: el elemento está en la lista. Si no, False. 
    """
    encontrado = False
    for i in range(len(lista)):
        if lista[i] == elemento:
            encontrado = True
    return encontrado

def mostrar_lista_colores(lista: list):
    """Imprime en consola todos los elementos de una lista, separados por espacios.

    Args:
        lista (list): Lista a mostrar
    """
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()  # salto de línea

def normalizar_palabra(palabra:str)->str:
    """Elimina espacios al inicio y final de una palabra y la convierte en mayúscula.

    Args:
        palabra (str): Palabra a normalizar

    Returns:
        str: Palabra sin espacios ni mayúsculas.
    """
    palabra = mi_strip(palabra)
    palabra = Mi_Upper(palabra)
    return palabra

def validar_input(valor_validacion:any , valor_comparar:any)-> bool:
    """Solicita nuevamente un valor si es igual al valor no permitido.

    Args:
        valor_validacion (any): Valor actual que se está verificando
        valor_comparar (any): Valor con el que no debe coincidir

    Returns:
        bool: True: valor válido.
    """
    while valor_validacion == valor_comparar:
        secreto = input("Palabra inválida. Ingrese una palabra correcta:  ")
        secreto = normalizar_palabra(secreto)
    return True