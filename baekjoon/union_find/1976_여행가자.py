import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
parent = [i for i in range(n)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j]:
            union(i, j)
plan = list(map(lambda x: int(x) - 1, input().split()))
p = find(plan[0])
for i in range(1, len(plan)):
    if p != find(plan[i]):
        print('NO')
        exit()
print('YES')