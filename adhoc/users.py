
import json

def user(li):
    s = " ".join(li)
    if s.endswith(","):
        s = s[:-1]
    u = json.loads(s)
    print u

with open("users.txt", "r") as f:
    buf = list()
    for line in f:
        line = line.strip()
        if not line:
            user(buf)
            buf = list()
        else:
            buf.append(line)

if len(buf) > 0:
    user(buf)
