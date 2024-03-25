import sys
input = sys.stdin.readline
n = int(input())
graph = [[sys.maxsize] * n for _ in range(n)]
for x in range(n):
    graph[x][x] = 0

for i in range(n):
    row = []
    for idx, j in enumerate(input().rstrip()):
        if i == idx:
            continue
        if j == 'Y':
            graph[i][idx] = 1
for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]
res = 0
for i in range(n):
    row = 0
    for j in range(n):
        if i == j:
            continue
        if graph[i][j] <= 2:
            row += 1
    res = max(res, row)
print(res)
