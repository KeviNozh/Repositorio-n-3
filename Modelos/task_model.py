from .base_model import BaseModel

class TaskModel(BaseModel):
    def __init__(self, task_id, user_id, description):
        self.task_id = task_id
        self.user_id = user_id
        self.description = description
