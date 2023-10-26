import socket
import threading
import random
import string
import os
import shutil
# Importa la función de generación de códigos desde el archivo genid.py en la carpeta services
from src.services.genid import genid_groups
from src.services.genid import genid_user

# Configuración de servidor
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 88888       # Puerto del servidor

# Directorio donde se almacenarán los datos
data_dir = "src/database/"

# Diccionario para almacenar los servidores y sus clientes
servers = {}

import argparse

# Crear un analizador de argumentos
parser = argparse.ArgumentParser(description="Descripción de tu programa")

# Agregar argumentos personalizados
parser.add_argument("--start", action="store_true", help="Iniciar el programa")

# Analizar los argumentos de la línea de comandos
args = parser.parse_args()

# Verificar si se proporcionó el argumento --start
if args.start:
    # Coloca aquí el código para iniciar el programa
    print("El programa ha sido iniciado.")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    logo = """
Yb    dP 88 .dP"Y8 88  dP"Yb  88b 88 888888 Yb  dP    Yb        dP  db  Yb    dP 888888 
 Yb  dP  88 `Ybo." 88 dP   Yb 88Yb88 88__    YbdP      Yb  db  dP  dPYb  Yb  dP  88__   
  YbdP   88 o.`Y8b 88 Yb   dP 88 Y88 88""    dPYb       YbdPYbdP  dP==Yb  YbdP   88""   
   YP    88 8bodP' 88  YbodP  88  Y8 888888 dP  Yb       YP  YP  dP    Yb  YP    888888 
                 """
    print(logo)






def main():
    while True:
        clear_console()  # Limpia la consola
        print_logo()  # Muestra el logo ASCII
        show_menu()
        choice = input("Selecciona una opción (1/2/3/4/5): ")
        
        if choice == '1':
            create_group()
        elif choice == '2':
            join_group()
        elif choice == '3':
            show_user_groups()
        elif choice == '4':
            new_agent()
        elif choice == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
        input("Presiona Enter para continuar...")



# Función para manejar la conexión de un cliente
def handle_client(client_socket, server_name):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                print(f"Cliente desconectado del servidor {server_name}")
                break
            # Manejar los datos recibidos (puedes definir tu lógica aquí)
            print(f"Datos recibidos en el servidor {server_name}: {data.decode()}")
    except Exception as e:
        print(f"Error en el servidor {server_name}: {str(e)}")
    client_socket.close()

# Función para crear un nuevo servidor
def create_server(server_name):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Servidor {server_name} escuchando en {HOST}:{PORT}")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexión aceptada desde {addr[0]}:{addr[1]} en el servidor {server_name}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, server_name))
        client_handler.start()

def create_user():
    username = input("Nombre de usuario: ")
    user_code = genid_user()  # Genera un código único para el usuario

    # Código para agregar al usuario a los grupos por defecto
    add_user_to_default_groups(username, ["Grupo-Noticias", "Grupo-Novedades"])

    # Lógica para crear el usuario y asignar el código (añade tu lógica aquí)
    print(f"Usuario '{username}' creado con el código único: {user_code}")


def add_user_to_default_groups(username, default_groups):
    # Carga la información de grupos desde el archivo groups.txt
    groups_data = load_data("groups.txt")

    for group in default_groups:
        if username not in groups_data:
            groups_data[username] = []

        if group not in groups_data[username]:
            groups_data[username].append(group)

    # Guarda la información de grupos de nuevo en el archivo
    save_data("groups.txt", groups_data)


# Lógica para unirse a un grupo/servidor
def join_group():
    # Lógica para unirse a un grupo/servidor (añade tu lógica aquí)
    group_name = input("Ingresa el nombre del grupo/servidor al que deseas unirte: ")
    user_code = genid_groups()  # Genera un código único para el usuario
    print(f"Te has unido al grupo/servidor '{group_name}' con el código único de usuario: {user_code}")


def save_group(group_data):
    with open(os.path.join(data_dir, "groups.txt"), 'a') as file:
        file.write(f"{group_data['nombre']}:{group_data['codigo']}\n")

def genid_groups():
    # Genera un código único para el grupo (puedes personalizar la generación)
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))


def save_group(group_data):
    with open(os.path.join(data_dir, "groups.txt"), 'a') as file:
        file.write(f"{group_data['nombre']}:{group_data['codigo']}\n")

# Función para mostrar el menú
def show_menu():
    print("Menú:")
    print("1. Crear un nuevo grupo/servidor")
    print("2. Unirse a un grupo/servidor")
    print("3. Mostrar grupos suscritos")  # Opción para mostrar grupos suscritos
    print("4. Nuevo agente")  # Opción para crear un nuevo agente
    print("5. Salir")

def show_user_groups():
    username = input("Nombre de usuario: ")
    
    # Cargar los grupos en los que está el usuario
    user_groups = load_data("groups.txt")

    if username not in user_groups:
        print(f"El usuario '{username}' no está en ningún grupo.")
    else:
        print(f"Grupos en los que está el usuario '{username}':")
        for group in user_groups[username]:
            print(group)

# Nueva función para crear un nuevo agente
def new_agent():
    # Lógica para crear un nuevo agente (añade tu lógica aquí)
    username = input("Nombre de usuario: ")
    user_code = genid_user()  # Genera un nuevo código único para el usuario
    # Lógica para eliminar al usuario anterior y crear uno nuevo (añade tu lógica aquí)
    print(f"Nuevo agente '{username}' creado con el código único: {user_code}")

def save_data(filename, data):
    with open(os.path.join(data_dir, filename), 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def load_data(filename):
    data = []
    file_path = os.path.join(data_dir, filename)
    if not os.path.exists(file_path):
        return data  # El archivo no existe, devolvemos una lista vacía

    with open(file_path, 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

def new_agent():
    # Elimina el archivo de usuarios si existe
    users_file = os.path.join(data_dir, "users.txt")
    if os.path.exists(users_file):
        os.remove(users_file)

    # Crea un nuevo agente generando un código único
    user_code = genid_user()
    
    # Guarda el código del nuevo agente en el archivo de usuarios
    users_data = load_data("users.txt")
    users_data.append(user_code)
    save_data("users.txt", users_data)

# Ejemplo de cómo cargar y mostrar los usuarios
def show_user_groups():
    user_groups = load_data("groups.txt")
    for group in user_groups:
        print(group)

def create_group():
    # Lógica para crear un nuevo grupo (añade tu lógica aquí)
    server_name = input("Nombre del grupo/servidor: ")
    # Genera un código único para este grupo
    group_code = genid_groups()
    # Lógica para crear el grupo y guardar el código (añade tu lógica aquí)

    # Crear un diccionario para representar el grupo
    group_data = {
        "nombre": server_name,
        "codigo": group_code
    }

    # Guarda el grupo en el archivo "groups.txt"
    save_group(group_data)

    print(f"Grupo/servidor '{server_name}' creado con el código único: {group_code}")


if __name__ == "__main__":
    main()
