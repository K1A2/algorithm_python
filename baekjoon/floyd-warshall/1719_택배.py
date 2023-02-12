import sys
INF = 1e10
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[[INF, -1] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = [c, b]
    graph[b][a] = [c, a]
for i in range(n):
    graph[i][i] = [0, -1]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j][0] > graph[i][k][0] + graph[k][j][0]:
                graph[i][j] = [graph[i][k][0] + graph[k][j][0], graph[i][k][1]]
for i in range(n):
    for j in range(n):
        print('-' if graph[i][j][1] == -1 else graph[i][j][1] + 1, end=' ')
    print()
