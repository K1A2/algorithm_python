import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
data = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for d in dxy:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < m and data[x][y] > data[nx][ny]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]
print(dfs(0, 0))