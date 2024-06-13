import sys
input = lambda : sys.stdin.readline()
r, c, k = map(int, input().split())
data = [list(input().rstrip()) for _ in range(r)]
dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def dfs(x, y, count, result):
    if x == 0 and y == c - 1 and count == k:
        return result + 1
    for d in dxy:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < r and 0 <= ny < c and data[nx][ny] != 'T':
            data[nx][ny] = 'T'
            result = dfs(nx, ny, count + 1, result)
            data[nx][ny] = '.'
    return result
data[r - 1][0] = 'T'
print(dfs(r - 1, 0, 1, 0))
