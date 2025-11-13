from archivos import *
from manejo_juego import *
def main():
    print("=== LOGIN ===")
    nombre = input("Usuario: ")
    contraseña = input("Contraseña: ")

    # 🔹 Login o registro de usuario
    usuario = login_usuario(nombre, contraseña)
    if not usuario:
        print("¿Deseas registrarte? (s/n): ", end="")
        if input().lower() == "s":
            registrar_usuario(nombre, contraseña)
            usuario = login_usuario(nombre, contraseña)
        else:
            print("Saliendo del juego...")
            return

    # 🔹 Una vez logueado, pasamos al menú principal
    print(f"\nBienvenido/a {nombre}! Cargando el menú del juego...\n")
    menu()  # 👈 Aquí llamas a tu menú del juego (ya existente)


if __name__ == "__main__":
        main()