# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N=int(input())
for i in range(N):
    if re.match(r'^[789]\d{9}$',input()):
        print("YES")
    else:
        print("NO")

