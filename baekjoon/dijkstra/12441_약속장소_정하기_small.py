import sys
input = sys.stdin.readline
for c in range(int(input())):
    n, p, m = map(int, input().split())
    friends = [list(map(int, input().split())) for _ in range(p)]
    graph = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        road = list(map(int, input().split()))
        for i in range(1, road[1]):
            graph[road[1 + i]][road[2 + i]] = graph[road[2 + i]][road[1 + i]] = road[0]

    for k in range(1, n + 1):
        graph[k][k] = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    res = sys.maxsize
    for i in range(1, n + 1):
        r = 0
        check = 0
        for f in friends:
            if graph[i][f[0]] != sys.maxsize:
                check += 1
                r = max(r, graph[i][f[0]] * f[1])
        if check == p:
            res = min(res, r)
    print(f'Case #{c + 1}: {res if res != sys.maxsize else -1}')
