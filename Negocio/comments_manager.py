class CommentsManager:
    def __init__(self, api_handler):
        self.api_handler = api_handler

    def get_comments(self):
        return self.api_handler.handle_get("/comments")

    def create_comment(self, comment_data):
        return self.api_handler.handle_post("/comments", comment_data)

    def update_comment(self, comment_id, comment_data):
        return self.api_handler.handle_put(f"/comments/{comment_id}", comment_data)

    def delete_comment(self, comment_id):
        return self.api_handler.handle_delete(f"/comments/{comment_id}")
