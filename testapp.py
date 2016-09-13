#
# pow test app
#

from models.user import User

u=User()
u.metadata.create_all(u.engine)
u.schema()

