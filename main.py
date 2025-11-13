from archivos import *
from manejo_juego import *
def main():
    x=cargar_config()
    print("=== LOGIN ===")
    nombre = input("Usuario: ")
    contraseña = input("Contraseña: ")

    # 🔹 Login o registro de usuario
    usuario = login_usuario(nombre, contraseña)
    if not usuario:
        entrada = input("¿Deseas registrarte? (s/n): ", end="")
        entrada = normalizar_palabra(entrada)
        if entrada == "S":
            registrar_usuario(nombre, contraseña)
            usuario = login_usuario(nombre, contraseña)
        else:
            print("Saliendo del juego...")
            return

    # 🔹 Una vez logueado, pasamos al menú principal
    print(f"\nBienvenido/a {nombre}! Cargando el menú del juego...\n")
    inicializar_estadisticas(usuario["nombre"])  # Aseguramos que las estadísticas estén inicializadas
    menu(usuario)  


if __name__ == "__main__":
        main()