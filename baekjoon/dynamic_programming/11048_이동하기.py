import sys
input = sys.stdin.readline
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        can = [0]
        if j - 1 >= 0:
            can.append(maze[i][j - 1])
        if i - 1 >= 0:
            can.append(maze[i - 1][j])
        if j - 1 >= 0 and i - 1 >= 0:
            can.append(maze[i - 1][j - 1])
        maze[i][j] += max(can)
print(maze[-1][-1])
