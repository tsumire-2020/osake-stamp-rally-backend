from pydantic import BaseModel

class AlcoholSchema(BaseModel):
  id: int
  name: str

