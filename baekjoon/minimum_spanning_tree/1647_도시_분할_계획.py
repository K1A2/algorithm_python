import sys
v, e = map(int, sys.stdin.readline().rstrip().split())
graph = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(e)]
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
result = []
for g in graph:
    a, b, c = g
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result.append(c)
print(sum(result[:-1]))