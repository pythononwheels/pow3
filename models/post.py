#
# Model
#
from config.config import Base
from sqlalchemy import Column, Integer, String, Sequence
from pow3.db import engine, Session
from pow3.models.basemodels.postbase import PostBase
from pow3.powlib import relation



class Post(PostBase):
   pass