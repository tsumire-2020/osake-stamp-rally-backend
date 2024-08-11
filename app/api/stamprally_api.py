from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.extensions import get_db
from app.models.stamprally_model import StampRally
from app.schemas.stamprally_schema import CreateStamprallySchema

stamprally_router = APIRouter()

@stamprally_router.get("/stamprallies/{stamprally_id}")
def get_stamprally(stamprally_id:int, db: Session = Depends(get_db)):
  return db.query(StampRally).filter(StampRally.id == stamprally_id).first()

@stamprally_router.get("/stamprallies")
def get_stamprallies(db: Session= Depends(get_db)):
  return db.query(StampRally).all()

@stamprally_router.post("/stamprallies")
def create_stamprally(stamprally: CreateStamprallySchema, db: Session = Depends(get_db)):
  # Todo Userの追加
  new_stamprally = StampRally(**stamprally.model_dump())
  db.add(new_stamprally)
  db.commit()
  db.refresh(new_stamprally)
  return new_stamprally