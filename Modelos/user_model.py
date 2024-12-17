from .base_model import BaseModel

class UserModel(BaseModel):
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
