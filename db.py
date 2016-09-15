#
#
#
from config.config import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


conn_str = db["type"]+"://"+db["user"]+":"+db["passwd"]+"@"+db["host"]+":"+str(db["port"])+"/"+db["name"]

engine = create_engine(conn_str)
Session = sessionmaker(bind=engine)
session = Session()



from sqlalchemy.ext.declarative import declarative_base
from pow3.models.basemodels.basemodel import BaseModel

Base = declarative_base(cls=BaseModel)
Base.metadata.bind = engine
Base.metadata.reflect(extend_existing=True)