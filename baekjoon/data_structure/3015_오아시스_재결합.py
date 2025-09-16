import sys
from collections import deque
input = sys.stdin.readline
data = deque()
n = int(input())
ans = 0
for _ in range(n):
    a = int(input())

    while data and data[-1][0] < a:
        p = data.pop()
        ans += p[1]
    if data and data[-1][0] == a:
        ans += data[-1][1]
        data[-1][1] += 1
        if len(data) > 1:
            ans += 1
    else:
        if data:
            ans += 1
        data.append([a, 1])
print(ans)
