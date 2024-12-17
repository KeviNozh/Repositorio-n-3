class AlbumsManager:
    def __init__(self, api_handler):
        self.api_handler = api_handler

    def get_albums(self):
        return self.api_handler.handle_get("/albums")

    def create_album(self, album_data):
        return self.api_handler.handle_post("/albums", album_data)

    def update_album(self, album_id, album_data):
        return self.api_handler.handle_put(f"/albums/{album_id}", album_data)

    def delete_album(self, album_id):
        return self.api_handler.handle_delete(f"/albums/{album_id}")
