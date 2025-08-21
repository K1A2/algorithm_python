
def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b, cycle):
    pa = find(parent, a)
    pb = find(parent, b)
    if pa == pb or cycle[a] == 1 or cycle[b] == 1:
        cycle[a] = cycle[b] = cycle[pa] = cycle[pb] = 1
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

case = 1
while 1:
    n, m = map(int, input().split())
    if n == m == 0: break
    parent = [i for i in range(n + 1)]
    cycle = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        union(parent, a, b, cycle)

    res = set()
    for i in range(1, n + 1):
        p = find(parent, i)
        if cycle[p] == 1:
            continue
        res.add(p)
    res = len(res)
    if res == 0:
        print(f'Case {case}: No trees.')
    elif res == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {res} trees.')
    case += 1
