from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.extensions import get_db
from app.models.user_model import User

user_router = APIRouter()


@user_router.get("/user")
def get_stamprallies(db: Session= Depends(get_db)):
  return db.query(User).all()

@user_router.post("/user/register")
def register_user(db: Session=Depends(get_db)):
  # Todo UseMake
  return None