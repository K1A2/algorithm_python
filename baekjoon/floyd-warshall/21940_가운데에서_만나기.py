import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[sys.maxsize] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
h = int(input())
friends = list(map(int, input().split()))

for k in range(1, n + 1):
    graph[k][k] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

round = [0] * (n + 1)
for i in range(1, n + 1):
    for f in friends:
        if i == f or graph[i][f] == sys.maxsize or graph[f][i] == sys.maxsize:
            continue
        round[i] = max(round[i], graph[i][f] + graph[f][i])

ans = [1]
m = round[1]
for i in range(2, n + 1):
    if m == round[i]:
        ans.append(i)
    elif m > round[i]:
        ans = [i]
        m = round[i]
print(*ans)
