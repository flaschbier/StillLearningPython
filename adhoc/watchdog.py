import time
import glob
import os
import hashlib


def md5(filename):
    with open(filename, 'rb') as inputfile:
        data = inputfile.read()
        print hashlib.md5(data).hexdigest()

path_to_watch = "."
before = os.listdir(path_to_watch)
while 1:
    time.sleep (3)
    after = os.listdir(path_to_watch)
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added:
        print "Added: ", ", ".join(added)
        for filename in added:
            md5(filename)
    if removed: print "Removed: ", ", ".join(removed)
    before = after
