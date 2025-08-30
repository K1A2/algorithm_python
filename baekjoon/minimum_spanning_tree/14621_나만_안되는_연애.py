import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(lambda x: 0 if x == 'M' else 1, input().split()))

path = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    if data[a] == data[b]: continue
    heapq.heappush(path, (c, a, b))

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
while path:
    c, a, b = heapq.heappop(path)
    if union(a, b):
        ans += c

if groups > 1:
    print(-1)
else:
    print(ans)
