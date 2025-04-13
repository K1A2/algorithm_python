import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
a, b = map(int, input().split())

q = deque()
q.append((a, 0))
visited = [0] * (n + 1)
visited[0] = 1
while q:
    now, count = q.popleft()
    nx = now
    i = 1
    while nx <= n:
        nx = now + data[now - 1] * i
        i += 1
        if 1 <= nx <= n and visited[nx] == 0:
            visited[nx] = 1
            if nx == b:
                print(count + 1)
                exit()
            q.append((nx, count + 1))
    nx = now
    i = 1
    while nx > 0:
        nx = now - data[now - 1] * i
        i += 1
        if 1 <= nx <= n and visited[nx] == 0:
            visited[nx] = 1
            if nx == b:
                print(count + 1)
                exit()
            q.append((nx, count + 1))
print(-1)
