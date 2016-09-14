#
# pow test app
#

from models.user import User
from models.Post import Post
from db import session, engine


u=User(name="klaas")
u.metadata.create_all(engine)


