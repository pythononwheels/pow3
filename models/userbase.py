#
# Model
#
from config.config import Base
from sqlalchemy import Column, Integer, String, Sequence
from db import engine, Session
from models.basemodel import BaseModel

class UserBase(Base,BaseModel):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    #id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    firstname = Column(String)
    lastname = Column(String)


    def __repr__(self):
        ostr=""
        for elem in self.__dict__:
            ostr += str(elem)
        return ostr

    def get_session(self):
        return self.session
    
    def table(self):
        return self.__table__ 
    
    def columns(self):
        return self.__table__._columns

    def column_names(self):
        pass

    def items(self):
        return self.__table__._columns.items()        

    def column_value(self, name):
        return self.__table__._columns[name]
