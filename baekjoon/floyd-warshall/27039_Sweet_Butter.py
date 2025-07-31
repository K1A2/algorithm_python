import sys
input = sys.stdin.readline
INF = int(1e10)
n, p, c = map(int, input().split())
cows = [int(input()) for _ in range(n)]
graph = [[INF] * (p + 1) for _ in range(p + 1)]
for _ in range(c):
    a, b, k = map(int, input().split())
    graph[a][b] = k
    graph[b][a] = k

for i in range(1, p + 1):
    graph[i][i] = 0

for k in range(1, p + 1):
    for i in range(1, p + 1):
        for j in range(1, p + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = INF
for i in range(1, p + 1):
    cmd = 0
    b = 0
    for cow in cows:
        if graph[i][cow] == INF:
            b = 1
            break
        cmd += graph[i][cow]
    if not b:
        ans = min(ans, cmd)
print(ans)
