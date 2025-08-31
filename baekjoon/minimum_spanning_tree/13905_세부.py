import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s, e = map(int, input().split())
bridges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(bridges, (-c, a - 1, b - 1))

groups = n
parent = [i for i in range(n)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    global groups
    x = find(x)
    y = find(y)
    if x == y: return 0
    groups -= 1

    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    return 1

while bridges:
    c, a, b = heapq.heappop(bridges)
    union(a, b)
    if find(s - 1) == find(e - 1):
        print(-c)
        exit()
print(0)
