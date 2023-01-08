import sys
input = sys.stdin.readline
n, m = map(int, input().split())
x, y, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]
dxy = ((-1, 0), (0, 1), (1, 0), (0, -1))
result = 0
check[x][y] = 1
if not data[x][y]:
    result += 1
while 1:
    is_clean = 0
    for i in range(1, 5):
        left_idx = (d - i) % 4
        nx, ny = x + dxy[left_idx][0], y + dxy[left_idx][1]
        if 0 <= nx < n and 0 <= ny < m and not data[nx][ny] and not check[nx][ny]:
            x, y = nx, ny
            check[x][y] = 1
            result += 1
            d = left_idx
            is_clean = 1
            break
    if not is_clean:
        back_idx = (d + 2) % 4
        nx, ny = x + dxy[back_idx][0], y + dxy[back_idx][1]
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny]:
            break
        x, y = nx, ny
print(result)
