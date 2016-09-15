#
# Model
#
from pow3.db import Base,engine, Session
from sqlalchemy import Column, Integer, String, Sequence
from pow3.powlib import relation
from pow3.models.post import Post

@relation.has_many(Post)
class User(Base):
    #__tablename__ = "users"
    #id = Column(Integer, primary_key=True)
    #id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    firstname = Column(String)
    lastname = Column(String)