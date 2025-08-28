from collections import deque
n, k = map(int, input().split())
world = [[-1] * n for _ in range(n)]
parent = [i for i in range(k)]
groups = k

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    global groups
    x = find(x)
    y = find(y)

    if x == y: return

    groups -= 1

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))

q = deque()
for c in range(k):
    a, b = map(int, input().split())
    world[a - 1][b - 1] = c
    x = a - 1
    y = b - 1
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if world[nx][ny] >= 0 and world[nx][ny] != world[x][y]:
                union(world[x][y], world[nx][ny])
            elif world[nx][ny] == -1:
                q.append((nx, ny, c))
                world[nx][ny] = -2

nq = deque()
ans = 0
while 1:
    if groups == 1:
        break
    while q:
        x, y, c = q.popleft()
        if world[x][y] >= 0: continue
        world[x][y] = c
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if world[nx][ny] >= 0 and world[nx][ny] != world[x][y]:
                    union(world[x][y], world[nx][ny])
                elif world[nx][ny] == -1:
                    nq.append((nx, ny, c))
                    world[nx][ny] = -2
    ans += 1
    q, nq = nq, deque()
print(ans)
