import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if x == y:
            graph[x][y] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

s = [sum([j if j != INF else 0 for j in graph[i]]) for i in range(1, n + 1)]
reslut = (s[0], 1)
for i in range(1, n):
    if reslut[0] > s[i]:
        reslut = (s[i], i + 1)
    elif reslut[0] == s[i] and reslut[1] > i:
        reslut = (s[i], i + 1)
print(reslut[1])