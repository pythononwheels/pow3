#
#
#
from config.config import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

conn_str = db["type"]+"://"+db["user"]+":"+db["passwd"]+"@"+db["host"]+":"+str(db["port"])+"/"+db["name"]
print("trying to connect to: " + conn_str)
engine = create_engine(conn_str)
Session = sessionmaker(bind=engine)


def get_session():
    return Session()

def get_engine():
    return engine


session = get_session()