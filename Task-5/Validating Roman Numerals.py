Thousand = 'M{0,3}'
Hundred = '(C[MD]|D?C{0,3})'
Ten = '(X[CL]|L?X{0,3})'
Digit = '(I[VX]|V?I{0,3})'
regex_pattern = r"%s%s%s%s$" % (Thousand, Hundred, Ten, Digit) # Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))