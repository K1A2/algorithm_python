import sys
from collections import deque
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n = int(input())
price = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(n):
    a = list(map(int, list(input().rstrip())))
    for j in range(n):
        if a[j]:
            graph[i + 1].append(j + 1)

index = 1
parent = [0] * (n + 1)
finished = [0] * (n + 1)
q = deque()
res = 0

def dfs(node):
    global index, res
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
            scc.append(price[now - 1])
            finished[now] = 1
            if now == node:
                break
        res += min(scc)
    return low

for i in range(1, n + 1):
    if parent[i] == 0:
        dfs(i)

print(res)
