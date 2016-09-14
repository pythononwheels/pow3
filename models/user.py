#
# Model
#
from pow3.config.config import Base
from sqlalchemy import Column, Integer, String, Sequence
from pow3.db import engine, Session
from pow3.models.basemodels.userbase import UserBase
from pow3.powlib import relation
from pow3.models.post import Post

@relation.has_many(Post)
class User(UserBase):
   pass