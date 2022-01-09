from sys import stdin
from collections import deque
alen, blen = map(int, stdin.readline().rstrip().split())
a = deque([i for i in map(int, stdin.readline().rstrip().split())])
b = deque([i for i in map(int, stdin.readline().rstrip().split())])
result = []
while True:
    if len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            result.append(b.popleft())
        else:
            result.append(a.popleft())
    elif len(a) == 0 and len(b) > 0:
        result += list(b)
        b.clear()
    elif len(b) == 0 and len(a) > 0:
        result += list(a)
        a.clear()
    else:
        break
print(' '.join([str(i) for i in result]))