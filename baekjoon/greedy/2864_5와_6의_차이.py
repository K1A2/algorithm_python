import re
a, b = input().split()
f2s = lambda c: re.sub("6", "5", c)
s2f = lambda c: re.sub("5", "6", c)
print(int(f2s(a)) + int(f2s(b)), int(s2f(a)) + int(s2f(b)))
