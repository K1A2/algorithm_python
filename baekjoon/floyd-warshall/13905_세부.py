INF = int(1e10)
n = int(input())
d = int(input())
graph = [[INF] * n for _ in range(n)]
for i in range(n):
    data = list(input().rstrip())
    for j in range(n):
        if data[j] == 'Y':
            graph[i][j] = d
            graph[j][i] = d

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(-1)
            exit()
        ans = max(ans, graph[i][j])
print(ans)
