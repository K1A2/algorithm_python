from collections import deque

n, m, k = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dice = [1, 2, 3, 4, 5, 6] # top, back, right, left, front, bottom

def roll_dice(direction, x, y):
    if ((direction == 0 and x == 0) or (direction == 1 and y == m - 1)
            or (direction == 2 and x == n - 1) or (direction == 3 and y == 0)):
        direction = (direction + 2) % 4

    if direction == 1: # e
        y += 1
        new_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif direction == 3: # w
        y -= 1
        new_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif direction == 0: # n
        x -= 1
        new_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif direction == 2: # s
        x += 1
        new_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

    if new_dice[-1] > map_data[x][y]:
        direction = (direction + 1) % 4
    elif new_dice[-1] < map_data[x][y]:
        direction = (direction + 3) % 4

    return direction, x, y, new_dice

def find_same(x, y, visit_idx):
    q = deque()
    q.append((x, y))
    visited[x][y] = visit_idx
    target = map_data[x][y]
    count = 1
    while q:
        x, y = q.pop()
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx = x + dx
            ny = y + dy
            if (0 <= nx < n and 0 <= ny < m and
                    map_data[nx][ny] == target and visited[nx][ny] < visit_idx):
                visited[nx][ny] = visit_idx
                count += 1
                q.append((nx, ny))
    return count

direction = 1 # 0 t, 1 r, 2 b, 3 l
x = y = 0
ans = 0
visited_idx = 1
for _ in range(k):
    direction, x, y, dice = roll_dice(direction, x, y)
    ans += find_same(x, y, visited_idx) * map_data[x][y]
    visited_idx += 1
print(ans)
