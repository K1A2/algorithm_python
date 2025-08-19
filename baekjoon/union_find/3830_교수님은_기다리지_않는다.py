import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(parent, weight, a):
    if parent[a] != a:
        pa = find(parent, weight, parent[a])
        weight[a] += weight[parent[a]]
        parent[a] = pa
    return parent[a]

def union(parent, weight, diff, a, b):
    pa = find(parent, weight, a)
    pb = find(parent, weight, b)

    if pa == pb: return

    pdiff = weight[a] - weight[b] + diff
    if pdiff >= 0:
        parent[pb] = pa
        weight[pb] = pdiff
    else:
        parent[pa] = pb
        weight[pa] = abs(pdiff)

while 1:
    n, m = map(int, input().split())
    if n == m == 0: break

    parent = [0] * (n + 1)
    weight = [0] * (n + 1)
    for i in range(1, n):
        parent[i] = i

    for _ in range(m):
        query = input().rstrip().split()
        a = int(query[1])
        b = int(query[2])
        if query[0] == '!':
            union(parent, weight, int(query[3]), a, b)
        else:
            find(parent, weight, a)
            find(parent, weight, b)
            if parent[a] != parent[b]:
                print('UNKNOWN')
                continue
            print(weight[b] - weight[a])
