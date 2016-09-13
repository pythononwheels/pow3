#
# Model
#
from config.config import Base
from sqlalchemy import Column, Integer, String, Sequence
from db import engine, Session
from models.basemodel import BaseModel

class UserBase(Base,BaseModel):
    __tablename__ = "user"
    #id = Column(Integer, primary_key=True)
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String(30))
    session = Session()
    engine = engine

    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)
    def get_session(self):
        return self.session