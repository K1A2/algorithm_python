import sys
input = sys.stdin.readline
INF = 10e10
n, m = map(int, input().split())
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = c
for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
ans = INF
for i in range(n):
    for j in range(n):
        if 0 < graph[i][j] < INF and 0 < graph[j][i] < INF:
            ans = min(ans, graph[i][j] + graph[j][i])
print(ans if ans != INF else -1)
