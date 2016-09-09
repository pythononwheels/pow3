#
# Model
#
from config.config import Base
from sqlalchemy import Column, Integer, String, Sequence
from db import engine, Session
from models.userbase import UserBase

class User(UserBase):
   pass