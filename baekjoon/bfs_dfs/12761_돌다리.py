import sys
from collections import deque
input = sys.stdin.readline

a, b, n, m = map(int, input().rstrip().split())


def dx(i, x):
    if i == 0: return x - 1
    elif i == 1: return x + 1
    elif i == 2: return x - a
    elif i == 3: return x + a
    elif i == 4: return x - b
    elif i == 5: return x + b
    elif i == 6: return x * a
    elif i == 7: return x * b


q = deque()
q.append((n, 0))
visited = [0] * 100001
visited[n] = 1
while 1:
    now, count = q.popleft()
    for i in range(8):
        nx = dx(i, now)
        if 0 <= nx <= 100000 and visited[nx] == 0:
            if nx == m:
                print(count + 1)
                exit()
            q.append((nx, count + 1))
            visited[nx] = 1
