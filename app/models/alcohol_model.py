from app.extensions import Base
from sqlalchemy import Boolean, Column, Integer, String, DateTime

class Alcohol(Base):
  __tablename__ = "alcohol"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)