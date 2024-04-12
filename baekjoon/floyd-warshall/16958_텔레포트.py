import sys
input = sys.stdin.readline
n, t = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(n)]
graph = [[sys.maxsize] * n for _ in range(n)]
m = int(input())
xy = [list(map(int, input().split())) for _ in range(m)]
for i in range(n):
    t1, x1, y1 = cities[i]
    graph[i][i] = 0
    for j in range(i + 1, n):
        t2, x2, y2 = cities[j]
        if t1 == t2 == 1:
            graph[i][j] = graph[j][i] = min(t, abs(x1 - x2) + abs(y1 - y2))
        else:
            graph[i][j] = graph[j][i] = abs(x1 - x2) + abs(y1 - y2)

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for x, y in xy:
    print(graph[x - 1][y - 1])
