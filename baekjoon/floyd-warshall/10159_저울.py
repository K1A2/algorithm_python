import sys
input = sys.stdin.readline
INF = 10e10
n = int(input())
m = int(input())
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = 1
for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
for i in range(n):
    count = 0
    for j in range(n):
        if not (0 < graph[i][j] < INF) and not (0 < graph[j][i] < INF):
            count += 1
    sys.stdout.write(f'{count - 1}\n')
