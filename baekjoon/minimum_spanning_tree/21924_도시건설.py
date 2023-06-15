import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
graph = sorted(graph, key=lambda x: x[2])
parent = [i for i in range(n + 1)]
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

result = 0
for g in graph:
    a, b, c = g
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += c

connection = list(set(parent[1:]))
for i in range(len(connection)):
    for j in range(i + 1, len(connection)):
        if find(parent, connection[i]) != find(parent, connection[j]):
            print(-1)
            exit()
print(sum([i[2] for i in graph]) - result)
