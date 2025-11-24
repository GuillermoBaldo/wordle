# mi_slicing 
def rebanar(cadena: str, inicio: int, finalizacion: int, reverse: bool = False  ) -> str:
    """Devuelve una subcadena de 'cadena' entre las posiciones 'inicio' y 'finalizacion'. 
    Si 'reverse' es False, la subcadena se obtiene en orden normal. 
    Si 'reverse' es True, la subcadena se obtiene en orden inverso.

    Args:
        cadena (str): Cadena original de la cual se extraerá una parte.
        inicio (int): Índice inicial (incluido) desde donde comenzar a copiar.
        finalizacion (int): Índice final (no incluido) hasta donde copiar.
        reverse (bool, optional): Indica si la subcadena debe devolverse invertida. Por defecto es False.

    Returns:
        str: La subcadena obtenida según los parámetros indicados.
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
    """Convierte una letra de minúscula a mayúscula o viceversa, según el valor del parámetro.

    Args:
        letra (str): Letra a convertir.
        es_minucula (bool, optional): Si es True, convierte una letra minúscula a mayúscula. Si es False, convierte una mayúscula a minúscula. Por defecto es True.

    Returns:
    """

    if es_minucula:
        resultado = chr(ord(letra) - 32)
    else:
        resultado = chr(ord(letra) + 32)
    return resultado

def Mi_Upper(cadena: str) -> str:
    """Convierte todas las letras minúsculas de una cadena a mayúsculas.

    Args:
        cadena (str): Cadena de texto a convertir.

    Returns:
        str: Cadena con todas sus letras en mayúsculas.
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
    """Convierte todas las letras mayúsculas de una cadena a minúsculas.

    Args:
        cadena (str): Cadena de texto a convertir.

    Returns:
        str: Cadena con todas sus letras en minúsculas.
    """
    cadena_minuscula = ""
    for letra in range(len(cadena)):
        caracter = cadena[letra]
        letra_minuscula = caracter
        if caracter >= "A" and caracter <= "Z":  # si el caracter está entre 'a' y 'z'
            letra_minuscula = invertir_letra(caracter, False)
        cadena_mayuscula += letra_minuscula
    return cadena_minuscula

def Mi_capitalize(cadena: str) -> str:
    """Convierte la primera letra de una cadena a mayúscula y el resto a minúscula.

    Args:
        cadena (str): Cadena de texto a capitalizar.

    Returns:
        str: Cadena con la primera letra en mayúscula y las demás en minúscula.
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
    """Elimina los caracteres indicados (por defecto espacios) al inicio y al final de una cadena.

    Args:
        texto (str): Texto a procesar.
        caracter (str, optional): Carácter a eliminar de los extremos. Por defecto es espacio.

    Returns:
        str: Texto sin los caracteres de los extremos.
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
    """Verifica si una cadena contiene únicamente letras y espacios.

    Args:
        cadena (str): Cadena a verificar.

    Returns:
        bool: True si la cadena contiene solo letras o espacios, False en caso contrario.
    """
    resultado= True
    for letra in range (len(cadena)):
        caracter = cadena[letra]
        if not ((caracter >= "A" and caracter <= "Z") or (caracter >= "a" and caracter <= "z") or caracter == " "):
            resultado= False
    return resultado

def es_int(cadena: str) -> bool:
    """Verifica si una cadena representa un número entero o decimal válido.

    Args:
        cadena (str): Cadena a verificar.

    Returns:
        bool: True si la cadena contiene solo dígitos o un punto decimal, False en caso contrario.
    """
    resultado= True
    for letra in range (len(cadena)):
        caracter = cadena[letra]
        if not (caracter >= "0" and caracter <= "9" or caracter== ".") :
            resultado= False
    return resultado

def validar_letra(letra:str )-> str:
    """Valida que el valor ingresado sea una sola letra del alfabeto.

    Args:
        letra (str): Valor a validar.

    Returns:
        tuple[bool, str]: Una tupla con un booleano indicando si es válido y la letra en minúscula.
    """
    # valida que el ingreso sea una letra
    resultado = False
    if len(letra) == 1 and  es_string(letra):
        letra = Mi_Lower(letra)        
        resultado = True
    return resultado, letra

def buscar_indice(lista, elemento):
    """Busca un elemento en una lista y devuelve el índice de su primera aparición.

    Args:
        lista (list): Lista donde buscar.
        elemento (any): Elemento a buscar.

    Returns:
        int: Índice del elemento si se encuentra, -1 en caso contrario.
    """
    indice = -1
    for i in range(len(lista)):
        if lista[i] == elemento and indice == -1:
            indice = i
    return indice

def contiene(lista, elemento):
    """Verifica si un elemento está presente en una lista.

    Args:
        lista (list): Lista donde buscar.
        elemento (any): Elemento a verificar.

    Returns:
        bool: True si el elemento está en la lista, False en caso contrario.
    """
    encontrado = False
    for i in range(len(lista)):
        if lista[i] == elemento:
            encontrado = True
    return encontrado

def normalizar_palabra(palabra:str)->str:
    """Elimina espacios al inicio y final de una palabra y la convierte a mayúsculas.

    Args:
        palabra (str): Palabra a normalizar.

    Returns:
        str: Palabra sin espacios y en mayúsculas.
    """
    palabra = mi_strip(palabra)
    palabra = Mi_Upper(palabra)
    return palabra

def validar_input(valor_validacion:any , valor_comparar:any)-> bool:
    """Solicita nuevamente un valor si es igual al valor no permitido.

    Args:
        valor_validacion (any): Valor actual que se está verificando.
        valor_comparar (any): Valor con el que no debe coincidir.

    Returns:
        bool: True una vez que se ingresa un valor válido.
    """
    while valor_validacion == valor_comparar:
        secreto = input("Palabra inválida. Ingrese una palabra correcta:  ")
        secreto = normalizar_palabra(secreto)
    return True