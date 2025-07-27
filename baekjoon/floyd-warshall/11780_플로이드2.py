import sys
input = sys.stdin.readline

INF = int(1e10)
n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
path = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    path[a][b] = [a, b]

for i in range(n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = path[i][k] + path[k][j][1:]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            graph[i][j] = 0
        sys.stdout.write(f'{graph[i][j]} ')
    sys.stdout.write('\n')

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j: sys.stdout.write('0\n')
        elif len(path[i][j]) == 0: sys.stdout.write('0\n')
        else: sys.stdout.write(f'{len(path[i][j])} {" ".join(map(str, path[i][j]))}\n')
