data = [list(map(int, input().split())) for _ in range(5)]
numbers = set()

def dfs(num, x, y, depth):
    if depth == 6:
        numbers.add(num)
        return
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(num * 10 + data[nx][ny], nx, ny, depth + 1)

for i in range(5):
    for j in range(5):
        dfs(0, i, j, 0)
print(len(numbers))
