import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda a:a[2])
parents = [i for i in range(n)]

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]
def uion(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

ans = 0
for e in edges:
    start, end, cost = e
    start -= 1
    end -= 1
    if find(start) != find(end):
        ans += cost
        uion(start, end)
print(ans)
