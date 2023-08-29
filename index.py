import subprocess

# Base de datos simulada de usuarios y contraseñas (esto debería ser almacenado de manera segura)
users_database = {
    'usuario1': 'contrasena1',
    'usuario2': 'contrasena2',
    # Agrega más usuarios y contraseñas aquí
}

def login():
    username = input("Usuario: ")
    password = input("Contraseña: ")

    if username in users_database and users_database[username] == password:
        print("Inicio de sesión exitoso.")
    else:
        print("Usuario o contraseña incorrectos.")

def main():
    print("Bienvenido al sistema de inicio de sesión.")
    while True:
        print("\nOpciones:")
        print("1. Iniciar sesión")
        print("2. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            # Compilar el programa C++
            compilation_result = subprocess.run(["g++", "mi_programa.cpp", "-o", "mi_programa"], capture_output=True, text=True)

            if compilation_result.returncode == 0:
                print("Compilación exitosa. Ejecutando el programa...")
            execution_result = subprocess.run(["./mi_programa"], capture_output=True, text=True)

            if execution_result.returncode == 0:
                print("Ejecución exitosa. Salida del programa:")
                print(execution_result.stdout)
            else:
                print("Error durante la ejecución del programa:")
                print(execution_result.stderr)
        else:
            print("Error durante la compilación:")
            print(compilation_result.stderr)





        if choice == '2':
            print("Hasta luego.")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()