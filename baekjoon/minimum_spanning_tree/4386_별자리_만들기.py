import sys
import math
v = int(sys.stdin.readline().rstrip())
positions = [tuple(map(float, sys.stdin.readline().rstrip().split())) for _ in range(v)]
graph = []
for i in range(v):
    for j in range(i + 1, v):
        graph.append((i, j, math.sqrt((positions[i][0] - positions[j][0]) ** 2 + (positions[i][1] - positions[j][1]) ** 2)))
graph = sorted(graph, key=lambda x:x[2])
parent = [0] * (v + 1)
result = 0
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]
def union(parent, a, b):
    roota = find(parent, a)
    rootb = find(parent, b)
    if roota < rootb:
        parent[rootb] = roota
    else:
        parent[roota] = rootb
for i in range(1, v + 1):
    parent[i] = i
for g in graph:
    a, b, c = g
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += c
print(result)