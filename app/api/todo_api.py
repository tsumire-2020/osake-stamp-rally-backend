from fastapi import APIRouter


todo_router = APIRouter()

@todo_router.get("/todos")
def get_todos():
  return {"message":"Get all todos"}