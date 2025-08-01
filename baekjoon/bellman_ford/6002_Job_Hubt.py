INF = int(1e10)
d, p, c, f, s = map(int, input().split())
edges = []
for _ in range(p):
    a, b = map(int, input().split())
    edges.append((a, b, -d))
for _ in range(f):
    a, b, e = map(int, input().split())
    edges.append((a, b, -d + e))

dist = [INF] * (c + 1)
dist[s] = -d
for _ in range(c - 1):
    for u, v, w in edges:
        if dist[u] != INF and dist[v] > dist[u] + w:
            dist[v] = dist[u] + w

for u, v, w in edges:
    if dist[u] != INF and dist[v] > dist[u] + w:
        print(-1)
        exit()

print(-min(dist))
