from Servicios.api_service import ApiService

class RequestHandler:
    def __init__(self, base_url, api_key):
        self.api_service = ApiService(base_url, api_key)

    def get_albums(self):
        return self.api_service.get("/albums")

    def create_album(self, album_data):
        return self.api_service.post("/albums", album_data)

    def update_album(self, album_id, album_data):
        return self.api_service.put(f"/albums/{album_id}", album_data)

    def delete_album(self, album_id):
        return self.api_service.delete(f"/albums/{album_id}")

    def get_posts(self):
        return self.api_service.get("/posts")

    def create_post(self, post_data):
        return self.api_service.post("/posts", post_data)

    def update_post(self, post_id, post_data):
        return self.api_service.put(f"/posts/{post_id}", post_data)

    def delete_post(self, post_id):
        return self.api_service.delete(f"/posts/{post_id}")

    def get_todos(self):
        return self.api_service.get("/todos")

    def create_todo(self, todo_data):
        return self.api_service.post("/todos", todo_data)

    def update_todo(self, todo_id, todo_data):
        return self.api_service.put(f"/todos/{todo_id}", todo_data)

    def delete_todo(self, todo_id):
        return self.api_service.delete(f"/todos/{todo_id}")
