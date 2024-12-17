from base_model import BaseModel

class CommentModel(BaseModel):
    def __init__(self, comment_id, post_id, text):
        self.comment_id = comment_id
        self.post_id = post_id
        self.text = text
