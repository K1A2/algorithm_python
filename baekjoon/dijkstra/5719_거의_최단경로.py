import sys
import heapq
from collections import deque
input = lambda: sys.stdin.readline()

def dijkstra():
    distance = [sys.maxsize] * n
    parents = [[] for _ in range(n)]
    q = [(0, start)]
    distance[start] = 0
    while q:
        current_distance, current_node = heapq.heappop(q)
        if distance[current_node] < current_distance:
            continue
        for idx in range(len(graph[current_node])):
            next_node, weight, activate = graph[current_node][idx]
            if not activate:
                continue
            next_dist = current_distance + weight
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                parents[next_node] = [(current_node, idx)]
                heapq.heappush(q, (next_dist, next_node))
            elif next_dist == distance[next_node]:
                parents[next_node].append((current_node, idx))
    return distance, parents

def find_all_paths(parents, start):
    stack = deque([start])
    visited = [0] * n
    while stack:
        current = stack.pop()
        if not parents[current] or visited[current]:
            continue
        visited[current] = 1
        for p, idx in parents[current]:
            graph[p][idx][2] = 0
            stack.append(p)

if __name__ == '__main__':
    while 1:
        n, m = map(int, input().split())
        if n == m == 0:
            break
        start, end = map(int, input().split())

        graph = [[] for _ in range(n)]
        for _ in range(m):
            a, b, c = map(int, input().split())
            graph[a].append([b, c, 1])

        _, parents = dijkstra()
        find_all_paths(parents, end)

        dist, _ = dijkstra()
        print(-1 if dist[end] == sys.maxsize else dist[end])
