from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n)]
lines = [tuple(map(int, input().split())) for _ in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def ccw(a, b, c):
    t = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    if t > 0: return 1
    if t < 0: return -1
    return 0

def intersect(a, b, c, d):
    ab1 = ccw(a, b, c)
    ab2 = ccw(a, b, d)
    cd1 = ccw(c, d, a)
    cd2 = ccw(c, d, b)
    if ab1 == 0 and ab2 == 0:
        return (max(min(a[0], b[0]), min(c[0], d[0])) <= min(max(a[0], b[0]), max(c[0], d[0])) and
                max(min(a[1], b[1]), min(c[1], d[1])) <= min(max(a[1], b[1]), max(c[1], d[1])))
    return ab1 * ab2 <= 0 and cd1 * cd2 <= 0

for i in range(n):
    for j in range(i + 1, n):
        pi = find(i)
        pj = find(j)
        if pi == pj: continue

        x1, y1, x2, y2 = lines[i]
        x3, y3, x4, y4 = lines[j]
        a, b, c, d = (x1, y1), (x2, y2), (x3, y3), (x4, y4)
        if intersect(a, b, c, d):
            union(i, j)

count = defaultdict(int)
for p in parent:
    count[find(p)] += 1
v = list(count.values())
print(len(v))
print(max(v))
