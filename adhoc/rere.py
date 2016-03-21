import re


pattern = r"^-1|[\\d]+$"

for s in ["-1", "17"]:
    print re.match(pattern, s)
