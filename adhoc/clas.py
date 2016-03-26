class Data:
    def __init__(self):
        pass
    def vars(self):
        return self.__dict__

d = Data()
d.hurz = 5
print d.hurz
print d.vars()
print d.__dict__


a = [ "f1", "f2", "f3"]
b = [ "f2" ]
s = [ f for f in a if not f in b ]
print s
