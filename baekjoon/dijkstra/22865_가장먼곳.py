import sys
import heapq
input = sys.stdin.readline
n = int(input())
friends = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

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

dist_friends = []
for f in friends:
    dist_friends.append(dijkstra(f))

answer = 0
min_dist = 0
for i in range(1, n + 1):
    temp_dist = sys.maxsize
    for j in range(len(friends)):
        if dist_friends[j][i] != sys.maxsize:
            temp_dist = min(temp_dist, dist_friends[j][i])
    if temp_dist > min_dist:
        min_dist = temp_dist
        answer = i
print(answer)
