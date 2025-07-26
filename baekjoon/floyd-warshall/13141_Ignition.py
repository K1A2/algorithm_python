import sys
INF = int(1e10)
input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
distance = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    distance[a][b] = min(distance[a][b], c)
    distance[b][a] = min(distance[b][a], c)

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if x == y:
            distance[x][y] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

answer = INF
for s in range(1, n + 1):
    max_time = 0
    for u, v, L in edges:
        du = distance[s][u]
        dv = distance[s][v]
        if du > dv:
            du, dv = dv, du
        if dv - du >= L:
            t_edge = du + L
        else:
            t_edge = (du + dv + L) / 2
        if t_edge > max_time:
            max_time = t_edge

    if max_time < answer:
        answer = max_time
print(f"{answer:.1f}")
