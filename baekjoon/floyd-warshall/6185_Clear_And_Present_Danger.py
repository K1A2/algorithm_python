n, m = map(int, input().split())
visit = [int(input()) - 1 for _ in range(m)]
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
ans = 0
for i in range(1, m):
    ans += graph[visit[i - 1]][visit[i]]
print(ans)
