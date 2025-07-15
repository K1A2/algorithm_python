import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))
ta, tb = map(lambda x: int(x)-1, input().split())

def check(target):
    visited = [False]*n
    q = deque([ta])
    visited[ta] = True

    while q:
        u = q.popleft()
        if u == tb:
            return True
        for v, w in graph[u]:
            if not visited[v] and w >= target:
                visited[v] = True
                q.append(v)
    return False

low, high = 1, int(1e10)
while low <= high:
    mid = (low + high) // 2
    if check(mid):
        low = mid + 1
    else:
        high = mid - 1
print(high)
