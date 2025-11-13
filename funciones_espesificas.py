# mi_slicing 
def rebanar(cadena: str, inicio: int, finalizacion: int, reverse: bool = False  ) -> str:

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
    if es_minucula:
        resultado = chr(ord(letra) - 32)
    else:
        resultado = chr(ord(letra) + 32)
    return resultado

def Mi_Upper(cadena: str) -> str:
    cadena_mayuscula = ""
    for letra in range(len(cadena)):
        caracter = cadena[letra]
        letra_mayuscula = caracter
        if caracter >= "a" and caracter <= "z":  # si el caracter está entre 'a' y 'z'
            letra_mayuscula = invertir_letra(caracter)
        cadena_mayuscula += letra_mayuscula
    return cadena_mayuscula

def Mi_Lower(cadena: str) -> str:
    cadena_minuscula = ""
    for letra in range(len(cadena)):
        caracter = cadena[letra]
        letra_minuscula = caracter
        if caracter >= "A" and caracter <= "Z":  # si el caracter está entre 'a' y 'z'
            letra_minuscula = invertir_letra(caracter, False)
        cadena_mayuscula += letra_minuscula
    return cadena_minuscula

def Mi_capitalize(cadena: str) -> str:
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
    inicio = 0
    fin = len(texto) - 1
    while inicio <= fin and texto[inicio] == caracter:
        inicio += 1

    while fin >= inicio and texto[fin] == caracter:
        fin -= 1

    resultado = texto[inicio:fin+1]
    return resultado

def es_string(cadena: str) -> bool:
    resultado= True
    for letra in range (len(cadena)):
        caracter = cadena[letra]
        if not ((caracter >= "A" and caracter <= "Z") or (caracter >= "a" and caracter <= "z") or caracter == " "):
            resultado= False
    return resultado

def es_int(cadena: str) -> bool:
    resultado= True
    for letra in range (len(cadena)):
        caracter = cadena[letra]
        if not (caracter >= "0" and caracter <= "9" or caracter== ".") :
            resultado= False
    return resultado


def validar_letra(letra:str )-> str:
    # valida que el ingreso sea una letra
    resultado = False
    if len(letra) == 1 and  es_string(letra):
        letra = Mi_Lower(letra)        
        resultado = True
    return resultado, letra

def buscar_indice(lista, elemento):
    """Devuelve el índice de la primera aparición del elemento o -1 si no está."""
    indice = -1
    for i in range(len(lista)):
        if lista[i] == elemento and indice == -1:
            indice = i
    return indice

def contiene(lista, elemento):
    """Devuelve True si el elemento está en la lista."""
    encontrado = False
    for i in range(len(lista)):
        if lista[i] == elemento:
            encontrado = True
    return encontrado

def mostrar_lista_colores(lista):
    """Imprime los elementos de una lista """
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()  # salto de línea

def normalizar_palabra(palabra:str)->str:
    palabra = mi_strip(palabra)
    palabra = Mi_Upper(palabra)
    return palabra

def validar_input(valor_validacion:any , valor_comparar:any)-> bool:
    while valor_validacion == valor_comparar:
        secreto = input("Palabra inválida. Ingrese una palabra correcta:  ")
        secreto = normalizar_palabra(secreto)
    return True