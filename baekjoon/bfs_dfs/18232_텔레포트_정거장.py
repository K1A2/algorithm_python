import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
s, e = map(int, input().split())
tp = dict()
for _ in range(m):
    a, b = map(int, input().split())
    try:
        tp[a].append(b)
    except:
        tp[a] = [b]
    try:
        tp[b].append(a)
    except:
        tp[b] = [a]

q = deque()
q.append((s, 0))
visited = [0] * (n + 1)
while q:
    now, count = q.popleft()
    dx = [now - 1, now + 1]
    try:
        for i in tp[now]:
            dx.append(i)
    except:
        pass
    for nx in dx:
        if 1 <= nx <= n and visited[nx] == 0:
            visited[nx] = 1
            if nx == e:
                print(count + 1)
                exit()
            q.append((nx, count + 1))
