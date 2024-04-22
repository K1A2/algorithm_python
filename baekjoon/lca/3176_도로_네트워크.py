import sys
from collections import deque
import math
input = sys.stdin.readline

n = int(input())
LOG = int(math.log2(n)) + 1

graph = [[] for _ in range(n + 1)]
depth = [0] * (n + 1)
parent = [[[0, 0, 0] for _ in range(LOG)] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

d = deque()
d.append((1, 1))
depth[1] = 1
while d:
    current_node, current_depth = d.pop()
    for next_node, distance in graph[current_node]:
        if depth[next_node]:
            continue
        depth[next_node] = current_depth + 1
        parent[next_node][0] = [current_node, distance, distance]
        d.append((next_node, current_depth + 1))

for i in range(1, LOG):
    for j in range(1, n + 1):
        parent[j][i][0] = parent[parent[j][i - 1][0]][i - 1][0]
        parent[j][i][1] = min(parent[parent[j][i - 1][0]][i - 1][1], parent[j][i - 1][1])
        parent[j][i][2] = max(parent[parent[j][i - 1][0]][i - 1][2], parent[j][i - 1][2])

def lca(a, b):
    path_min = sys.maxsize
    path_max = 0
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(LOG, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            path_min = min(path_min, parent[b][i][1])
            path_max = max(path_max, parent[b][i][2])
            b = parent[b][i][0]
    if a == b:
        return str(path_min), str(path_max)
    for i in range(LOG - 1, -1, -1):
        if parent[a][i][0] != parent[b][i][0]:
            path_min = min(path_min, parent[a][i][1], parent[b][i][1])
            path_max = max(path_max, parent[a][i][2], parent[b][i][2])
            a = parent[a][i][0]
            b = parent[b][i][0]
    path_min = min(path_min, parent[a][0][1], parent[b][0][1])
    path_max = max(path_max, parent[a][0][2], parent[b][0][2])
    return str(path_min), str(path_max)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(' '.join(lca(a, b)))
