from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from app.extensions import get_db
from app.models.stamprally_model import StampRally,Stamp
from app.models.alcohol_model import Alcohol
from app.schemas.stamprally_schema import CreateStamprallySchema, StampRallySchema

stamprally_router = APIRouter()

@stamprally_router.get("/stamprallies/{stamprally_id}", response_model=StampRallySchema)
def get_stamprally(stamprally_id:int, db: Session = Depends(get_db)):
  stamprally = db.query(StampRally).filter(StampRally.id == stamprally_id).first()

  # Todo スタンプラリーに紐づくスタンプを取得する
  # Todo　スタンプに紐づくスタンプを取得する
  return stamprally

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
  alcohols = db.query(Alcohol).order_by(func.random()).limit(4).all()
  for alcohol in alcohols:
    stamp = Stamp(stamp_rally_id = new_stamprally.id, alcohol_id=alcohol.id)
    db.add(stamp)
  db.commit()
  return {"id": new_stamprally.id}