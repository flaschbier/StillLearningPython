# this will break the test that assumes myconst.get_db_name is called
from myconst import get_db_name

def functio():
    return get_db_name()

print "inner:", functio()
