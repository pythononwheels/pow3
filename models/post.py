#
# Model
#
from pow3.db import Base,engine, Session
from sqlalchemy import Column, Integer, String, Sequence
from pow3.powlib import relation

class Post(Base):
    #__tablename__ = "posts"
    #id = Column(Integer, primary_key=True)
    #id = Column(Integer, Sequence('post_id_seq'), primary_key=True)
    title = Column(String)
    text = Column(String)
