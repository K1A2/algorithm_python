import sys
from collections import deque
n = int(input())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
d = deque()
result = [0]
d.append((nums[0], 0))
for i in range(1, n):
    while d:
        if d[-1][0] > nums[i]:
            result.append(d[-1][1] + 1)
            break
        else:
            d.pop()
    if not d:
        result.append(0)
    d.append((nums[i], i))
print(*result)