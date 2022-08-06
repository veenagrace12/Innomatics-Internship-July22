# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def change(match):
    if match.group(1) == '&&':
        return 'and'
    else:
        return 'or'

for i in range(int(input())):
    print(re.sub(r"(?<= )(\|\||&&)(?= )", change,input()))