from .base_model import BaseModel

class PostModel(BaseModel):
    def __init__(self, post_id, user_id, content):
        self.post_id = post_id
        self.user_id = user_id
        self.content = content
