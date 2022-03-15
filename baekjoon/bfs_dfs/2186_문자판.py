import sys
input = sys.stdin.readline
n, m, k = map(int, input().rstrip().split())
data = [input().rstrip() for _ in range(n)]
target = input().rstrip()
target_len = len(target) - 1
memory = [[[-1] * (target_len + 1) for _ in range(m)] for _ in range(n)]
def dfs(x, y, idx):
    if memory[x][y][idx] != -1:
        return memory[x][y][idx]
    if data[x][y] != target[idx]:
        return 0
    if idx == target_len:
        return 1
    c = 0
    for i in range(-k, k + 1):
        if not i:
            continue
        if 0 <= x + i < n:
            c += dfs(x + i, y, idx + 1)
        if 0 <= y + i < m:
            c += dfs(x, y + i, idx + 1)
    memory[x][y][idx] = c
    return c
count = 0
for x in range(n):
    for y in range(m):
        if data[x][y] == target[0]:
            count += dfs(x, y, 0)
print(count)