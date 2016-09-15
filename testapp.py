#
# pow test app
#

#from pow3.models.user import User
#from pow3.models.post import Post
#from pow3.db import session, engine


#u=User(firstname="klaas")
#u.metadata.create_all(engine)

import os
os.listdir("./models")

__all__ = []
_models = []

import pkgutil
import inspect

for loader, name, is_pkg in pkgutil.walk_packages(models.__path__):
    module = loader.find_module(name).load_module(name)
    print("module: " + name)
    for name, value in inspect.getmembers(module):
        print("member: " + name)
        if name.startswith('__'):
            continue

        #globals()[name] = value
        _models.append(name)
        #__all__.append(name)
print (_models)