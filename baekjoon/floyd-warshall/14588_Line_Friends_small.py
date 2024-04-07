import sys
input = sys.stdin.readline
n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
graph = [[sys.maxsize] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0
for i in range(n):
    x1, y1 = lines[i]
    for j in range(i + 1, n):
        x2, y2 = lines[j]
        if x1 <= x2 <= y1 or x2 <= x1 <= y2:
            graph[i][j] = 1
            graph[j][i] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
for _ in range(int(input())):
    a, b = map(int, input().split())
    r = graph[a - 1][b - 1]
    print(-1 if r == sys.maxsize else r)
