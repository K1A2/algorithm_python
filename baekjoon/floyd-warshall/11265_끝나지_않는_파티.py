import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[[sys.maxsize] for _ in range(n)] for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if i == j:
            graph[i][j] = 0
            continue
        graph[i][j] = a[j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(m):
    a, b, c = map(int, input().split())
    print('Enjoy other party' if graph[a - 1][b - 1] <= c else 'Stay here')
