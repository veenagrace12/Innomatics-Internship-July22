# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    lst = []
    s = input()
    for i in [r"[A-Z0-9]{10}", r"([A-Z].*){2,}", r"([0-9].*){3,}"]:
        lst.append(bool(re.search(i, s, flags=re.I)))
    if all(lst) is True:
        if bool(re.search(r".*(.).*\1.*", s)) is True:
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")