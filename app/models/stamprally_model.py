from app.extensions import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

class StampRally(Base):
  __tablename__ = "stamp_rally"
  # __table_args__ = {'extend_exsisting': True} 同じのを作るとでるえらー

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  description = Column(String, index=True)
  # user_id = Column(Integer, ForeignKey("user.id"))
  stamps = relationship("Stamp")
  # , back_populates="stamp_rally"を足すと逆引きが出来るようになるけどエラーする

class Stamp(Base):
  __tablename__ = "stamp"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  #TODO Alcoholに紐づける
  alcohol_id = Column(Integer, ForeignKey("alcohol.id"))
  stamp_rally_id = Column(Integer, ForeignKey("stamp_rally.id"))
  alcohol = relationship("Alcohol")

class StampResult(Base):
  __tablename__ = "stamp_result"

  id = Column(Integer, primary_key=True, index=True)
  stamp_id = Column(Integer, primary_key=True, index=True)
  is_stamped = Column(Boolean, index=True)
  stamp_date = Column(DateTime) 