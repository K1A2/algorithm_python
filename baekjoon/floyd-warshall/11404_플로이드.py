import sys
INF = int(1e9)
input = sys.stdin.readline
n = int(input())
data = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            data[i][j] = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    data[a][b] = min(data[a][b], c)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if data[i][j] == INF:
            sys.stdout.write(f'{0} ')
        else:
            sys.stdout.write(f'{data[i][j]} ')
    sys.stdout.write('\n')