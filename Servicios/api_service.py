import requests

class ApiService:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    def get(self, endpoint):
        try:
            response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en GET {endpoint}: {e}")
            return None

    def post(self, endpoint, data):
        try:
            response = requests.post(f"{self.base_url}{endpoint}", json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en POST {endpoint}: {e}")
            return None

    def put(self, endpoint, data):
        try:
            response = requests.put(f"{self.base_url}{endpoint}", json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en PUT {endpoint}: {e}")
            return None

    def delete(self, endpoint):
        try:
            response = requests.delete(f"{self.base_url}{endpoint}", headers=self.headers)
            response.raise_for_status()
            return {"message": "Eliminado correctamente"}
        except requests.exceptions.RequestException as e:
            print(f"Error en DELETE {endpoint}: {e}")
            return None
