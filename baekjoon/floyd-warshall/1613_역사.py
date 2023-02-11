import sys
input = sys.stdin.readline
INF = 10e10
n, m = map(int, input().split())
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
for i in range(n):
    graph[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
for _ in range(int(input())):
    a, b = map(int, input().split())
    if (graph[a - 1][b - 1] < 0 or graph[a - 1][b - 1] >= INF) and (graph[b - 1][a - 1] < 0 or graph[b - 1][a - 1] >= INF):
        print(0)
    elif graph[a - 1][b - 1] > graph[b - 1][a - 1]:
        print(1)
    elif graph[a - 1][b - 1] < graph[b - 1][a - 1]:
        print(-1)