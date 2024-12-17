import requests
import json

class SerperAPI:
    BASE_URL = "https://google.serper.dev"
    API_KEY = "4d801916a99bbfd6442849d098d459d0d42c3ca1"

    @staticmethod
    def get_search(query):
        """GET: Realiza una búsqueda general usando parámetros en la URL."""
        url = f"{SerperAPI.BASE_URL}/search?q={query.replace(' ', '+')}&apiKey={SerperAPI.API_KEY}"
        response = requests.get(url)
        return response.json()

    @staticmethod
    def post_search(query):
        """POST: Realiza una búsqueda general usando un payload JSON."""
        url = f"{SerperAPI.BASE_URL}/search"
        headers = {
            'X-API-KEY': SerperAPI.API_KEY,
            'Content-Type': 'application/json'
        }
        payload = json.dumps({"q": query})
        response = requests.post(url, headers=headers, data=payload)
        return response.json()

    @staticmethod
    def put_search(query, update_data):
        """PUT: Simula una actualización de datos."""
        url = f"{SerperAPI.BASE_URL}/search"
        headers = {
            'X-API-KEY': SerperAPI.API_KEY,
            'Content-Type': 'application/json'
        }
        payload = json.dumps({"q": query, "update": update_data})
        response = requests.put(url, headers=headers, data=payload)
        return {"status": "success", "message": "Simulación PUT exitosa", "data": response.json()}

    @staticmethod
    def delete_search(query):
        """DELETE: Simula la eliminación de una búsqueda."""
        url = f"{SerperAPI.BASE_URL}/search"
        headers = {
            'X-API-KEY': SerperAPI.API_KEY,
            'Content-Type': 'application/json'
        }
        payload = json.dumps({"q": query})
        response = requests.delete(url, headers=headers, data=payload)
        return {"status": "success", "message": "Simulación DELETE exitosa", "data": response.text}
