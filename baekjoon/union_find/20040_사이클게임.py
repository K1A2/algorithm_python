import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parents = [i for i in range(n)]

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i + 1)
        exit()
    union(a, b)
print(0)
