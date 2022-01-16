INF = int(1e9)
n = 4
m = 7
graph = [[1000000000, 1000000000, 1000000000, 1000000000, 1000000000],[1000000000, 0, 4, 1000000000, 6],
         [1000000000, 3, 0, 7, 1000000000], [1000000000, 5, 1000000000, 0, 4], [1000000000, 1000000000, 1000000000, 2, 0]]

for k in  range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('I', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()