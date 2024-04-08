import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
ans = 0
for i in range(n):
    left = 0
    right = 0
    for j in range(n):
        if i == j:
            continue
        elif graph[i][j] == 1:
            right += 1
        elif graph[j][i] == 1:
            left += 1
    if right > n // 2 or left > n // 2:
        ans += 1
print(ans)
