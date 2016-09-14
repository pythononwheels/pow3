#
# pow test app
#

from pow3.models.user import User
from pow3.models.Post import Post
from pow3.db import session, engine


u=User(name="klaas")
#u.metadata.create_all(engine)

import os
os.listdir("./models")

