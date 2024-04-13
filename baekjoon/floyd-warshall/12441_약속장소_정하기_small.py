import sys
import heapq
input = sys.stdin.readline
for c in range(int(input())):
    n, p, m = map(int, input().split())
    friends = [list(map(int, input().split())) for _ in range(p)]
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        road = list(map(int, input().split()))
        for i in range(1, road[1]):
            graph[road[1 + i]].append((road[2 + i], road[0]))
            graph[road[2 + i]].append((road[1 + i], road[0]))

    def dijkstra(start):
        q = []
        distance = [sys.maxsize] * (n + 1)
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for node, d in graph[now]:
                cost = dist + d
                if cost < distance[node]:
                    distance[node] = cost
                    heapq.heappush(q, (cost, node))
        return distance

    dist_f = []
    for start, time in friends:
        dij = dijkstra(start)
        for i in range(n + 1):
            dij[i] *= time
        dist_f.append(dij)

    res = sys.maxsize
    for i in range(1, n + 1):
        r = 0
        check = 0
        for j in range(p):
            if dist_f[j][i] // friends[j][1] != sys.maxsize:
                check += 1
                r = max(r, dist_f[j][i])
        if check == p:
            res = min(res, r)
    print(f'Case #{c + 1}: {res if res != sys.maxsize else -1}')
