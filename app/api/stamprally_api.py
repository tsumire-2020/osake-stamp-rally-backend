from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.extensions import get_db
from app.models.stamprally_model import StampRally
from app.schemas.stamprally_schema import CreateStamprallySchema

stamprally_router = APIRouter()

@stamprally_router.get("/stamprally")
def get_todos(db: Session= Depends(get_db)):
  return db.query(StampRally).all()

@stamprally_router.post("/stamprally")
def create_stamprally(stamprally: CreateStamprallySchema, db: Session = Depends(get_db)):
  new_stamprally = StampRally(**stamprally.dict())
  db.add(new_stamprally)
  db.commit()
  db.refresh(new_stamprally)
  return new_stamprally