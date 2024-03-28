import sys
input = sys.stdin.readline
n = int(input())
graph = [[sys.maxsize] * n for _ in range(n)]
while 1:
    a, b = map(lambda x: int(x) - 1, input().split())
    if a == b == -2:
        break
    graph[a][b] = 1
    graph[b][a] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
res = []
for i in range(n):
    s = 0
    for j in range(n):
        if i != j and graph[i][j] != sys.maxsize:
            s = max(s, graph[i][j])
    res.append((s, i))
res = sorted(res, key=lambda x: x[0])
asw = [i for i in res if i[0] == res[0][0]]
print(asw[0][0], len(asw))
print(' '.join([str(i[1] + 1) for i in asw]))
