
import json

all_examples = ['A,1,1', 'B,2,1', 'C,4,4', 'D,4,5']
ll = [ x.split(",") for x in all_examples ]
ld = list()
for col in range(1, len(ll[0])):
    ld.append({ l[0] : int(l[col]) for l in ll })
print ld

print json.dumps(ld, indent=4)
"""
    dictionary = [
        {"A":1, "B":2, "C":4, "D":4 },
        {"A":1, "B":1, "C":4, "D":5 }
        ]
"""
