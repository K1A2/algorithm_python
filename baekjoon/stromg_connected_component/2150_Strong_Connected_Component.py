import sys
from collections import deque
sys.setrecursionlimit(int(10e5))
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

index = 1
parent = [0] * (v + 1)
finished = [0] * (v + 1)
q = deque()
res = []

def dfs(node):
    global index
    index += 1
    parent[node] = low = index
    q.append(node)

    for g in graph[node]:
        if parent[g] == 0:
            low = min(low, dfs(g))
        else:
            if finished[g] == 0:
                low = min(low, parent[g])

    if low == parent[node]:
        scc =[]
        while q:
            now = q.pop()
            scc.append(now)
            finished[now] = 1
            if now == node:
                break
        scc.sort()
        res.append(scc)
    return low

for i in range(1, v + 1):
    if parent[i] == 0:
        dfs(i)
sys.stdout.write(f'{len(res)}\n')
res.sort(key=lambda x:x[0])
for r in res:
    r.append(-1)
    sys.stdout.write(f'{" ".join(map(str, r))}\n')
