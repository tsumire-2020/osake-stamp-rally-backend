from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.extensions import get_db
from app.models.todo_model import Todo
from app.schemas.todo_schema import CreateTodoSchema

todo_router = APIRouter()

@todo_router.get("/todos")
def get_todos(db: Session= Depends(get_db)):
  return db.query(Todo).all()

@todo_router.post("/todos")
def create_todo(todo:CreateTodoSchema, db: Session= Depends(get_db)):
  new_todo = Todo(**todo.dict())
  db.add(new_todo)
  db.commit()
  db.refresh(new_todo)

  return new_todo