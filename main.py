from manejoJSON import *
from manejo_juego import *
def main():
    usuario = login()
    if usuario != None:
        inicializar_estadisticas(usuario["nombre"])  # Aseguramos que las estadísticas estén inicializadas
        menu(usuario)  


def login():
    opcion = input("Primera vez jugando?(s/n): ")
    opcion = normalizar_palabra(opcion)
    usuario = None
    
    if opcion == "S":
        print("=== REGISTRO DE USUARIO ===")
        print(f"Ingresa tus datos para registrarte")
        nombre = input("Elige un nombre de usuario: ")
        contraseña = input("Elige una contraseña: ")
        reingreso = input("Reingresa la contraseña: ")
        while contraseña != reingreso:
            print("Las contraseñas no coinciden. Intenta nuevamente.")
            contraseña = input("Elige una contraseña: ")
            reingreso = input("Reingresa la contraseña: ")
        registrar_usuario(nombre, contraseña)
        print("Registro exitoso. Ahora puedes iniciar sesión.")
        usuario = login_usuario(nombre, contraseña)
        
    else:
        print("=== INICIO DE SESIÓN ===")
        nombre = input("Usuario: ")
        contraseña = input("Contraseña: ")
        usuario = login_usuario(nombre, contraseña)
    return usuario

if __name__ == "__main__":
        main()