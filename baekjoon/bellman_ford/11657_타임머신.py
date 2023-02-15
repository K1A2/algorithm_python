import sys
INF = 1e11
input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a - 1, b - 1, c))
dis = [INF] * n
dis[0] = 0
def bellman_ford():
    for i in range(n):
        for a, b, c in edges:
            if dis[a] != INF and dis[b] > dis[a] + c:
                dis[b] = dis[a] + c
                if i == n - 1:
                    print(-1)
                    exit()
bellman_ford()
for i in range(1, n):
    print(dis[i] if dis[i] != INF else -1)
