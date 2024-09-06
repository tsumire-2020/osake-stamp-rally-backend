from pydantic import BaseModel, ConfigDict
from typing import List
from app.schemas.alcohol_schema import AlcoholSchema

class CreateStamprallySchema(BaseModel):
  title: str
  description: str

class StampSchema(BaseModel):
  id: int
  alcohol: AlcoholSchema

class StampRallySchema(BaseModel):
  id: int
  title: str
  description: str
  stamps: List[StampSchema]
  # class Config:
  #   orm_mode = True

  # model_config= ConfigDict(from_attributes=True)
