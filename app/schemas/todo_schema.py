from pydantic import BaseModel

class CreateTodoSchema(BaseModel):
  title: str
  description: str
  completed: bool = False