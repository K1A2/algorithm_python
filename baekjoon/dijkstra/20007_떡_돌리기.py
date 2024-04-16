import sys
import heapq
input = sys.stdin.readline
n, m, x, y = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    distance = [sys.maxsize] * n
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

s = dijkstra(y)
can = []
check = 0
for d in range(n):
    if s[d] != sys.maxsize and d != y:
        if s[d] * 2 > x:
            print(-1)
            exit()
        can.append(s[d] * 2)
can = sorted(can)
if len(can) < n - 1:
    print(-1)
else:
    ans = 1
    dist = 0
    for i in range(n - 1):
        dist += can[i]
        if dist > x:
            dist = can[i]
            ans += 1
    print(ans)
