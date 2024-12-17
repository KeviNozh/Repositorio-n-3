from .base_model import BaseModel

class PhotoModel(BaseModel):
    def __init__(self, photo_id, album_id, url):
        self.photo_id = photo_id
        self.album_id = album_id
        self.url = url
