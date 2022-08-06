
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string=input()
m=re.escape(string) # for deleting characters,spaces & symbols
vowels = ' aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'
match = re.findall(r'(?<=[' + consonants + '])([' + vowels + ']{2,})(?=[' + consonants + '])',m,flags=re.I)

if len(match) > 0:
    print("\n".join(match))
else:
    print(-1)