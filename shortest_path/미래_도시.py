import sys
INF = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1
x, k = map(int, input().rstrip().split())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for l in range(1, n + 1):
            graph[j][l] = min(graph[j][l], graph[j][i] + graph[i][l])

distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)