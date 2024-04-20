import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start, end):
    q = [(0, start, 0)]
    distances = [[sys.maxsize, sys.maxsize] for _ in range(n)]
    distances[start] = [0, 0]

    while q:
        current_distance, current_node, current_path_length = heapq.heappop(q)
        if current_node == end and current_path_length == distances[end][1]:
            return current_distance

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            path_length = current_path_length + 1
            if (distances[neighbor][1] > path_length or (distances[neighbor][1] == path_length and distances[neighbor][0] > distance)):
                distances[neighbor] = (distance, path_length)
                heapq.heappush(q, (distance, neighbor, path_length))

    return sys.maxsize

print(dijkstra(0, 1))
