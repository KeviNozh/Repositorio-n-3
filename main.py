import requests
import json

API_KEY = "4d801916a99bbfd6442849d098d459d0d42c3ca1"
BASE_URL = "https://google.serper.dev/images"

def menu():
    print("\n=== Menú de Acceso ===")
    print("1. Autenticarse")
    print("2. Crear Usuario")
    print("3. Ejecutar GET")
    print("4. Ejecutar POST")
    print("5. Ejecutar PUT")
    print("6. Ejecutar DELETE")
    print("7. Salir")

def authenticate():
    print("\n--- Autenticación ---")
    username = input("Nombre de usuario: ").strip()
    password = input("Contraseña: ").strip()

    if not username or not password:
        print("Error: Nombre de usuario y contraseña son obligatorios.")
        return
    
    print(f"Usuario '{username}' autenticado exitosamente.")

def create_user():
    print("\n--- Crear Usuario ---")
    username = input("Nombre de usuario: ").strip()
    email = input("Correo electrónico: ").strip()

    if not username or not email:
        print("Error: Nombre de usuario y correo electrónico son obligatorios.")
        return
    
    print(f"Usuario '{username}' con email '{email}' creado exitosamente.")

def execute_api_request(method):
    print(f"\n--- Ejecutando {method} ---")
    
    if method == "GET":
        buscar = input("Ingrese el término de búsqueda (por ejemplo: 'Imagen'): ").strip()
        url = f"{BASE_URL}?q={buscar}&apiKey={API_KEY}"
        headers = {}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            print(f"Resultado GET: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error al ejecutar la solicitud GET: {e}")
    
    elif method == "POST":
        buscar = input("Ingrese el término de búsqueda para POST (por ejemplo: 'Imagen'): ").strip()
        url = BASE_URL
        payload = json.dumps({
            "q": buscar
        })
        headers = {
            'X-API-KEY': API_KEY,
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()
            print(f"Resultado POST: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error al ejecutar la solicitud POST: {e}")
    

if __name__ == "__main__":
    while True:
        menu()
        option = input("Seleccione una opción: ").strip()

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
            print("Saliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente nuevamente.")
