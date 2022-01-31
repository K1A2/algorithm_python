import sys
data = [list(map(int, list(sys.stdin.readline().rstrip()))) for i in range(9)]
zeros = []
for x in range(9):
    for y in range(9):
        if not data[x][y]:
            zeros.append((x, y))
def find(x, y):
    available = [1] * 10
    for n in range(9):
        available[data[n][y]] = 0
        available[data[x][n]] = 0
    check_x = 3 * (x // 3)
    check_y = 3 * (y // 3)
    for nx in range(check_x, check_x + 3):
        for ny in range(check_y, check_y + 3):
            if data[nx][ny]:
                available[data[nx][ny]] = 0
    return available
def backtracking(n):
    if n < len(zeros):
        x, y = zeros[n]
        check = find(x, y)
        for i in range(1, 10):
            if check[i]:
                data[x][y] = i
                backtracking(n + 1)
        data[x][y] = 0
    else:
        for i in data:
            for j in i:
                print(j, end='')
            print()
        exit()
backtracking(0)