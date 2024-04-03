import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

res_min = sys.maxsize
res = []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        r = sum([min(graph[i][k], graph[j][k]) * 2 for k in range(1, n + 1)])
        if res_min > r:
            res_min = r
            res = [i, j]
            continue
        if res_min == r:
            if res[0] > i:
                res_min = r
                res = [i, j]
                continue
            if res[0] == i and res[1] > j:
                res_min = r
                res = [i, j]
                continue
print(res[0], res[1], res_min)
