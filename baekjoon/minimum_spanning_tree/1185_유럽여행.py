import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
enter = [int(input()) for _ in range(n)]

paths = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    heapq.heappush(paths, (c + enter[b] + c + enter[a], a, b))

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

ans = 0
while paths:
    c, a, b = heapq.heappop(paths)
    if union(a, b):
        ans += c
    if groups == 1:
        break
print(ans + min(enter))
