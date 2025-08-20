g = int(input())
p = int(input())
parent = [i for i in range(g + 1)]

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

count = 0
for _ in range(p):
    tg = int(input())
    res = find(tg)
    if res == 0: break

    union(res, res - 1)
    count += 1
print(count)
