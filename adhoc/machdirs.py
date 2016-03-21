import os

path = ""
while True:
    nxt = raw_input("next level or empty to quit: ")
    if not nxt:
        break
    path = os.path.join(path, nxt)

print path
os.makedirs(path)


"""
    $ python machdirs.py
    next level or empty to quit: a
    next level or empty to quit: b
    next level or empty to quit: c
    next level or empty to quit:
    a/b/c
    $ find . -type d -print
    .
    ./a
    ./a/b
    ./a/b/c
    $
"""
