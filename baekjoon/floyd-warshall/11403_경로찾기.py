import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())

graph = []
for _ in range(n):
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] == 0:
            a[i] = INF
    graph.append(a)

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
for g in graph:
    for i in g:
        if i == INF:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()