#
# Model
#
from pow3.config.config import Base
from pow3.models.basemodels.basemodel import BaseModel
from sqlalchemy import Column, Integer, String, Sequence
from pow3.db import engine, Session
from pow3.powlib import relation

class Post(Base, BaseModel):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    #id = Column(Integer, Sequence('post_id_seq'), primary_key=True)
    title = Column(String)
    text = Column(String)
