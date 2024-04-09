import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c
    l = int(input())
    friends = list(map(int, input().split()))

    for k in range(1, n + 1):
        graph[k][k] = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    res = [sys.maxsize, -1]
    for i in range(1, n + 1):
        r = 0
        for f in friends:
            r += graph[i][f]
        if r < res[0]:
            res = [r, i]
    print(res[1])
