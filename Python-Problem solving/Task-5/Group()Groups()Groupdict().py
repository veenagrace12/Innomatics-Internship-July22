import re
string=input()
m = re.search(r'([a-zA-Z0-9])\1',string)
if m:
    print(m.group(1))
else:
    print(-1)
