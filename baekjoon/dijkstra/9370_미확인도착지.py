import sys
import heapq
INF = int(1e9)
def dijkstra(start, n):
    q = []
    distance = [INF for _ in range(n)]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next, cost_n in graph[now]:
            cost = dist + cost_n
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
    return distance
for _ in range(int(sys.stdin.readline().rstrip())):
    n, m, t = map(int, sys.stdin.readline().rstrip().split())
    s, g, h = map(int, sys.stdin.readline().rstrip().split())
    s -= 1
    g -= 1
    h -= 1
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        a -= 1
        b -= 1
        graph[a].append((b, c))
        graph[b].append((a, c))
    ds = dijkstra(s, n)
    dg = dijkstra(g, n)
    dh = dijkstra(h, n)
    asw = []
    for _ in range(t):
        target = int(sys.stdin.readline().rstrip())
        target -= 1
        if ds[target] >= ds[g] + dg[h] + dh[target] or ds[target] >= ds[h] + dh[g] + dg[target]:
            asw.append(target + 1)
    asw.sort()
    print(*asw)