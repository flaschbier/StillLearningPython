class Persistence:
    counter1 = 0
    def __init__(self):
        pass
    def additive(self, num):
        global counter1
        return counter1 # NameError:

c = Persistence()
print c.additive(5)

"""
Traceback (most recent call last):
  File "namend.py", line 10, in <module>
    print c.additive(5)
  File "namend.py", line 7, in additive
    return counter1 # NameError
NameError: global name 'counter1' is not defined
"""
