from manejoJSON import *
from manejo_juego import *
def main():
    usuario = login_completo()

    if usuario != None:
        print(f"\nBienvenido/a {usuario["nombre"]}! Cargando el menú del juego...\n")
        inicializar_estadisticas(usuario["nombre"])  # Aseguramos que las estadísticas estén inicializadas
        menu(usuario)  

def login_completo():
    print("=== LOGIN ===")
    nombre = input("Usuario: ")
    contraseña = input("Contraseña: ")

    # 🔹 Login o registro de usuario
    usuario = login_usuario(nombre, contraseña)
    resultado = None
    if not usuario:
        entrada = input("¿Deseas registrarte? (s/n): ", end="")
        entrada = normalizar_palabra(entrada)
        if entrada == "S":
            registrar_usuario(nombre, contraseña)
            usuario = login_usuario(nombre, contraseña)
            resultado = usuario
        else:
            print("Saliendo del juego...")
            resultado = None
    else:
        resultado = usuario
    return resultado

if __name__ == "__main__":
        main()