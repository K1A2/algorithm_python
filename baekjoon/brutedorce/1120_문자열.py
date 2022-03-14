import sys
a, b = sys.stdin.readline().rstrip().split()
l = len(b) - len(a)
asw = len(b)
for i in range(l + 1):
    na = b[:l - i] + a
    if i:
        na += b[-i:]
    c = 0
    for idx, i in enumerate(b):
        if na[idx] != i:
            c += 1
    asw = min(asw, c)
print(asw)