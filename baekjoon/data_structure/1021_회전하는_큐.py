import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
d = deque([i + 1 for i in range(n)])
count = [0, 0]
for target in map(int, sys.stdin.readline().rstrip().split()):
    target_idx = 0
    for i in range(n):
        if d[i] == target:
            target_idx = i
            break
    if target_idx == 0:
        d.popleft()
    else:
        if n % 2 == 0:
            if target_idx >= n // 2:
                d.rotate(n - target_idx)
                d.popleft()
                count[1] += n - target_idx
            else:
                d.rotate(-target_idx)
                d.popleft()
                count[0] += target_idx
        else:
            if target_idx <= n // 2:
                d.rotate(-target_idx)
                d.popleft()
                count[0] += target_idx
            else:
                d.rotate(n - target_idx)
                d.popleft()
                count[1] += n - target_idx
    n -= 1
print(sum(count))