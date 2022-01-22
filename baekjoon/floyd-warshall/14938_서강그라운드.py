import sys
inf = sys.maxsize
n, m, r = map(int, sys.stdin.readline().rstrip().split())
items = list(map(int, sys.stdin.readline().rstrip().split()))
graph = [[inf] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0
for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            graph[b][a] = graph[a][b]
result = 0
for i in graph:
    result = max(result, sum([items[j] if i[j] <= m else 0 for j in range(n)]))
print(result)