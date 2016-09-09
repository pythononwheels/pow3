#
# pow test app
#

from models import test


print(dir(test.Test))
print(test.Test.__table__)
print(test.Test.metadata)
t = test.Test()
print(t.__table__)