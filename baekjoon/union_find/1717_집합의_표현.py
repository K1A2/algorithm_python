import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    a, b, c = map(int, input().split())
    if not a:
        union(parent, b, c)
    else:
        print('YES' if find(parent, b) == find(parent, c) else 'NO')
