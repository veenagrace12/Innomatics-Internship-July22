# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
pattern = r'^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$'
for i in range(n):
    name, email = input().split(' ')
    if re.match(pattern, email):
        print(name, email)