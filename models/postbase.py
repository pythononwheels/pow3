#
# Model
#
from config.config import Base
from sqlalchemy import Column, Integer, String, Sequence
from db import engine, Session
from models.basemodel import BaseModel

class PostBase(Base,BaseModel):
    __tablename__ = "post"
    #id = Column(Integer, primary_key=True)
    id = Column(Integer, Sequence('post_id_seq'), primary_key=True)
    title = Column(String)
    text = Column(String)
    session = Session()

    def __repr__(self):
       return "<User(title='%s', text='%s')>" % (
                             self.title, self.text)
    def get_session(self):
        return self.session