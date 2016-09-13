#
# Model
#
from config.config import Base
from sqlalchemy import Column, Integer, String, Sequence
from db import engine, Session
from models.userbase import UserBase
from powlib import relation
from models.post import Post

@relation.has_many(Post)
class User(UserBase):
   pass