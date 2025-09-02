import sys
input = sys.stdin.readline
n, m = map(int, input().split())

paths = []
for _ in range(m + 1):
    a, b, c = map(int, input().split())
    paths.append((abs(c - 1), a, b))
paths.sort(key=lambda x: x[0])

parent = [i for i in range(n + 1)]
parent_w = [i for i in range(n + 1)]

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)
    if x == y: return 0

    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    return 1

ans_best = 0
ans_worst = 0
for i in range(m + 1):
    c, a, b = paths[i]
    wc, wa, wb = paths[m - i]

    if union(a, b, parent):
        ans_best += c
    if union(wa, wb, parent_w):
        ans_worst += wc
print(ans_worst ** 2 - ans_best ** 2)
