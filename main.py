from manejoJSON import *
from datos_juegos import *
from login import * 
def main() -> None:
    """Función principal del programa. Maneja el flujo inicial:
    realiza el login del usuario, inicializa sus estadísticas
    y muestra el menú principal.
    """
    usuario = login()
    if usuario != None:
        inicializar_estadisticas(usuario["nombre"])
        menu(usuario) 
    else: 
        print("No se pudo iniciar sesión. Saliendo del programa.") 

if __name__ == "__main__":
        main()