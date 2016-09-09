#
# Model
#
from config.config import Base
from sqlalchemy import Column, Integer, String, Sequence
from db import engine, Session
from models.postbase import PostBase

class Post(PostBase):
   pass