import requests

API_KEY = "4d801916a99bbfd6442849d098d459d0d42c3ca1"
BASE_URL = "https://api.serper.dev/"

def menu():
    print("=== Menú de Acceso ===")
    print("1. Autenticarse")
    print("2. Crear Usuario")
    print("3. Ejecutar GET")
    print("4. Ejecutar POST")
    print("5. Ejecutar PUT")
    print("6. Ejecutar DELETE")
    print("7. Salir")

def authenticate():
    print("Autenticando usuario...")
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    print(f"Usuario '{username}' autenticado exitosamente.")

def create_user():
    print("Creando nuevo usuario...")
    username = input("Nombre de usuario: ")
    email = input("Correo electrónico: ")
    print(f"Usuario '{username}' con email '{email}' creado exitosamente.")

def execute_api_request(method):
    endpoint = input("Ingrese el endpoint (por ejemplo: search): ")
    url = f"{BASE_URL}{endpoint}"
    headers = {"X-API-KEY": API_KEY}

    if method in ["POST", "PUT"]:
        data = input("Ingrese los datos en formato JSON: ")
    else:
        data = None

    response = requests.request(method, url, headers=headers, json=data)
    print(f"Respuesta ({method}):", response.json())

if __name__ == "__main__":
    while True:
        menu()
        option = input("Seleccione una opción: ")

        if option == "1":
            authenticate()
        elif option == "2":
            create_user()
        elif option == "3":
            execute_api_request("GET")
        elif option == "4":
            execute_api_request("POST")
        elif option == "5":
            execute_api_request("PUT")
        elif option == "6":
            execute_api_request("DELETE")
        elif option == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente nuevamente.")
