import sys
import heapq
INF = int(1e10)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c, (c / 2, c * 2)))
    graph[b].append((a, c, (c / 2, c * 2)))

def dijkstra(mode):
    q = [(0, mode, 1)]
    distance = [[INF] * (mode + 2) for _ in range(n + 1)]
    while q:
        dist, n_mode, node = heapq.heappop(q)
        if distance[node][1 - n_mode if n_mode != - 1 else 0] < dist: continue
        for n_node, n_cost, n_mcost in graph[node]:
            if mode == -1:
                cost = n_cost + dist
            else:
                cost = n_mcost[n_mode] + dist
            if distance[n_node][n_mode] > cost:
                distance[n_node][n_mode] = cost
                next_mode = n_mode
                if n_mode != -1:
                    next_mode = 1 - n_mode
                heapq.heappush(q, (cost, next_mode, n_node))
    distance[1] = [0] * (mode + 2)
    return distance

y = dijkstra(-1)
w = dijkstra(0)
print(sum([1 for i in range(1, n + 1) if y[i][0] < min(w[i]) and y[i][0] != INF and min(w[i]) != INF]))
