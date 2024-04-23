import sys
import math
from collections import deque
input = sys.stdin.readline

def init(a):
    d = deque()
    d.append((a, 1))
    depth[a] = 1
    while d:
        curr_node, curr_depth = d.pop()
        for next_node in graph[curr_node]:
            if depth[next_node]:
                continue
            depth[next_node] = curr_depth + 1
            parents[next_node][0] = curr_node
            d.append((next_node, curr_depth + 1))
    for j in range(1, LOG):
        for i in range(1, n + 1):
            parents[i][j] = parents[parents[i][j - 1]][j - 1]

def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parents[b][i]
    if a == b:
        return a
    for i in range(LOG - 1, -1, -1):
        if parents[a][i] != parents[b][i]:
            a = parents[a][i]
            b = parents[b][i]
    return parents[a][0]

for _ in range(int(input())):
    n = int(input())
    LOG = int(math.log2(n)) + 1
    graph = [[] for _ in range(n + 1)]
    root = -1
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        if root == -1 or root == b:
            root = a
    x, y = map(int, input().split())

    parents = [[0] * LOG for _ in range(n + 1)]
    depth = [0 for _ in range(n + 1)]
    init(root)

    print(lca(x, y))
