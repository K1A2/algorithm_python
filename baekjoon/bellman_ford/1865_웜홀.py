import sys
INF = 1e10
input = sys.stdin.readline
for _ in range(int(input())):
    n, m, w = map(int, input().split())
    dis = [INF] * n
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a - 1, b - 1, c))
        edges.append((b - 1, a - 1, c))
    for _ in range(w):
        a, b, c = map(int, input().split())
        edges.append((a - 1, b - 1, -c))
    dis[0] = 0
    def bellman_ford():
        for i in range(n):
            for a, b, c in edges:
                if dis[b] > dis[a] + c:
                    dis[b] = dis[a] + c
                    if i == n - 1:
                        return 'YES'
        return 'NO'
    print(bellman_ford())