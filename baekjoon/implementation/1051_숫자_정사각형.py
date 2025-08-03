import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = [list(map(int, list(input().rstrip()))) for _ in range(n)]
max_side = min(n, m)
for side in range(max_side, 1, -1):
    for x in range(0, n - side + 1):
        for y in range(0, m - side + 1):
            v = data[x][y]
            if data[x + side - 1][y] == v and data[x][y + side - 1] == v and data[x + side - 1][y + side - 1] == v:
                print(side * side)
                exit()
print(1)