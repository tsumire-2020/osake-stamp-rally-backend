from app.extensions import Base
from sqlalchemy import Boolean, Column, Integer, String, DateTime

class StampRally(Base):
  __tablename__ = "stamp_rally"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  description = Column(String, index=True)

class Stamp(Base):
  __tablename__ = "stamp"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  #TODO Alcoholに紐づける

class StampResult(Base):
  __tablename__ = "stamp_result"

  id = Column(Integer, primary_key=True, index=True)
  stamp_id = Column(Integer, primary_key=True, index=True)
  is_stamped = Column(Boolean, index=True)
  stamp_date = Column(DateTime) 