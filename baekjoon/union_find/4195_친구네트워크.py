import sys
input = sys.stdin.readline

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, size, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return size[a]
    else:
        if size[a] <= size[b]:
            parent[b] = parent[a]
            size[a] += size[b]
            return size[a]
        else:
            parent[a] = parent[b]
            size[b] += size[a]
            return size[b]

for _ in range(int(input())):
    n = int(input())
    parents = dict()
    count = dict()
    for _ in range(n):
        a, b = input().rstrip().split()
        for f in [a, b]:
            try:
                f = parents[f]
            except:
                parents[f] = f
                count[f] = 1
        print(union(parents, count, a, b))
