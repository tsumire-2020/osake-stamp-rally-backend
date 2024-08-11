from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.extensions import get_db
from app.models.alcohol_model import Alcohol
from app.schemas.stamprally_schema import CreateStamprallySchema

alcohol_router = APIRouter()


@alcohol_router.get("/alcohols")
def get_stamprallies(db: Session= Depends(get_db)):
  return db.query(Alcohol).all()