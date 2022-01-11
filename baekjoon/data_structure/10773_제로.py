from collections import deque
import sys
q = deque()
for _ in range(int(sys.stdin.readline().rstrip())):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        if len(q) != 0:
            q.pop()
    else:
        q.append(a)
print(sum(q))