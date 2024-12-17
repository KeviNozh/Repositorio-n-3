from Modelos.user_model import UserModel
from Servicios.request_handler import RequestHandler

class UserManager:
    def __init__(self, api_url, api_key):
        self.api_handler = RequestHandler(api_url, api_key)

    def create_user(self, user_data):
        self.api_handler.handle_post("/users", user_data)

    def get_users(self):
        return self.api_handler.handle_get("/users")

    def update_user(self, user_id, user_data):
        self.api_handler.handle_put(f"/users/{user_id}", user_data)

    def delete_user(self, user_id):
        self.api_handler.handle_delete(f"/users/{user_id}")
