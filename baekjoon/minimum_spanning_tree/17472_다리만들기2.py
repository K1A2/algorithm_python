from collections import deque, defaultdict
import heapq

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
points = defaultdict(list)
dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs(sx, sy, idx):
    q = deque()
    q.append((sx, sy))
    for ddx, ddy in dxy:
        nnx = sx + ddx
        nny = sy + ddy
        if 0 <= nnx < n and 0 <= nny < m and data[nnx][nny] == 0:
            points[idx].append((sx, sy))
            break
    data[sx][sy] = idx
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
                data[nx][ny] = idx
                q.append((nx, ny))
                for ddx, ddy in dxy:
                    nnx = nx + ddx
                    nny = ny + ddy
                    if 0 <= nnx < n and 0 <= nny < m and data[nnx][nny] == 0:
                        points[idx].append((nx, ny))
                        break

idx = 2
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            bfs(i, j, idx)
            idx += 1

dist = [[1000] * (idx - 2) for _ in range(idx - 2)]
for k, v in points.items():
    for p in v:
        for dx, dy in dxy:
            nx = p[0] + dx
            ny = p[1] + dy
            d = 1
            while 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] != 0:
                    if data[nx][ny] != k:
                        if d - 1 <= 1: break
                        dist[k - 2][data[nx][ny] - 2] = min(dist[k - 2][data[nx][ny] - 2], d - 1)
                        dist[data[nx][ny] - 2][k - 2] = min(dist[data[nx][ny] - 2][k - 2], d - 1)
                        break
                    else:
                        break
                nx += dx
                ny += dy
                d += 1
lines = []
for i in range(idx - 2):
    for j in range(i + 1, idx - 2):
        if dist[i][j] != 1000:
            heapq.heappush(lines, (dist[i][j], i, j))

parent = [i for i in range(idx - 2)]
groups = idx - 2

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
while lines:
    d, s, e = heapq.heappop(lines)
    res = union(s, e)
    if res == 1:
        ans += d

if groups != 1:
    print(-1)
else:
    print(ans)
