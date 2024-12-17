from .base_model import BaseModel

class AlbumModel(BaseModel):
    def __init__(self, album_id, title, user_id):
        self.album_id = album_id
        self.title = title
        self.user_id = user_id
