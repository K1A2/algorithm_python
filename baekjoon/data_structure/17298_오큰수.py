import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
data = deque(map(int, sys.stdin.readline().rstrip().split()))
asw = []
asw.append(-1)
max_v = deque([data.pop()])
prev = max_v[0]
while data:
    now = data.pop()
    if now < max_v[0]:
        if now < prev:
            asw.append(prev)
            max_v.append(prev)
        else:
            while max_v and max_v[-1] <= now:
                max_v.pop()
            if max_v:
                asw.append(max_v[-1])
            else:
                asw.append(-1)
                max_v.append(now)
    else:
        max_v.clear()
        max_v.append(now)
        asw.append(-1)
    prev = now
asw.reverse()
print(*asw)