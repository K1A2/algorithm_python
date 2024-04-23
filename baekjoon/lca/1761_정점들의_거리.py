import sys
import math
from collections import deque
input = sys.stdin.readline

n = int(input())
LOG = int(math.log2(n)) + 1
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

parents = [[[0, 0] for _ in range(LOG)] for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]

d = deque()
d.append((1, 1))
depth[1] = 1
while d:
    curr_node, curr_depth = d.pop()
    for next_node, cost in graph[curr_node]:
        if depth[next_node]:
            continue
        depth[next_node] = curr_depth + 1
        parents[next_node][0] = [curr_node, cost]
        d.append((next_node, curr_depth + 1))
for j in range(1, LOG):
    for i in range(1, n + 1):
        parents[i][j][0] = parents[parents[i][j - 1][0]][j - 1][0]
        parents[i][j][1] = parents[parents[i][j - 1][0]][j - 1][1] + parents[i][j - 1][1]

def lca(a, b):
    left = right = 0
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            right += parents[b][i][1]
            b = parents[b][i][0]
    if a == b:
        return left + right
    for i in range(LOG - 1, -1, -1):
        if parents[a][i][0] != parents[b][i][0]:
            left += parents[a][i][1]
            right += parents[b][i][1]
            a = parents[a][i][0]
            b = parents[b][i][0]
    return left + right + parents[a][0][1] + parents[b][0][1]

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lca(a, b))
