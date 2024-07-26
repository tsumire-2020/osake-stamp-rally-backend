from pydantic import BaseModel

class CreateStamprallySchema(BaseModel):
  title: str
  description: str