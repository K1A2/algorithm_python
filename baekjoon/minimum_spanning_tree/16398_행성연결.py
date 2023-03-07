import sys
input = sys.stdin.readline
n = int(input())

roads = []
for i in range(n):
    data = list(map(int, input().rstrip().split()))
    for j in range(n):
        if data[j]:
            roads.append((i, j, data[j]))
roads.sort(key=lambda x: x[2])

answer = 0
parents = [i for i in range(n)]

def find(target):
    if parents[target] != target:
        parents[target] = find(parents[target])
    return parents[target]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for r in roads:
    a, b, c = r
    if find(a) != find(b):
        answer += c
        union(a, b)

print(answer)
