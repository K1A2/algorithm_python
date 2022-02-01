import sys
v = int(sys.stdin.readline().rstrip())
positions = [tuple(map(int, (sys.stdin.readline().rstrip() + f' {idx}').split())) for idx in range(v)]
graph = []
cal = lambda a, b, c:abs(positions[a][c] - positions[b][c])
for s in range(3):
    positions = sorted(positions, key=lambda x: x[s])
    for i in range(v - 1):
        graph.append((positions[i][3], positions[i + 1][3], cal(i, i + 1, s)))
graph = sorted(graph, key=lambda x:x[2])
parent = [0] * v
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
for i in range(v):
    parent[i] = i
for g in graph:
    a, b, c = g
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += c
print(result)