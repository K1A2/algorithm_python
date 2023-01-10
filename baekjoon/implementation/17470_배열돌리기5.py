import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
change_log = list(map(int, input().split()))
x_mid = n // 2 - 1
y_mid = m // 2 - 1
x_max = n - 1
y_max = m - 1
check_data = [[[0, 0], [0, y_mid], [0, y_mid + 1], [0, y_max]],
              [[x_mid, 0], [x_mid, y_mid], [x_mid, y_mid + 1], [x_mid, y_max]],
              [[x_mid + 1, 0], [x_mid + 1, y_mid], [x_mid + 1, y_mid + 1], [x_mid + 1, y_max]],
              [[x_max, 0], [x_max, y_mid], [x_max, y_mid + 1], [x_max, y_max]]]
if n < 4 or m < 4:
    check_data = data
def flip(data, dir):
    n, m = len(data), len(data[0])
    if dir == 2:
        for i in range(n):
            for j in range(m // 2):
                data[i][j], data[i][m - j - 1] = data[i][m - j - 1], data[i][j]
    if dir == 1:
        for i in range(n // 2):
            for j in range(m):
                data[n - i - 1][j], data[i][j] = data[i][j], data[n - i - 1][j]
    return data
def rotate(data: list, dir):
    n, m = len(data), len(data[0])
    if dir > 4:
        new_data = [[0] * m for _ in range(n)]
        if dir == 5:
            for i in range(0, n // 2):
                for j in range(0, m // 2):
                    new_data[i][j + m // 2] = data[i][j]
                for j in range(m // 2, m):
                    new_data[i + n // 2][j] = data[i][j]
            for i in range(n // 2, n):
                for j in range(0, m // 2):
                    new_data[i - n // 2][j] = data[i][j]
                for j in range(m // 2, m):
                    new_data[i][j - m // 2] = data[i][j]
        else:
            for i in range(0, n // 2):
                for j in range(0, m // 2):
                    new_data[i + n // 2][j] = data[i][j]
                for j in range(m // 2, m):
                    new_data[i][j - m // 2] = data[i][j]
            for i in range(n // 2, n):
                for j in range(0, m // 2):
                    new_data[i][j + m // 2] = data[i][j]
                for j in range(m // 2, m):
                    new_data[i - n // 2][j] = data[i][j]
    else:
        new_data = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if dir == 3:
                    new_data[j][n - 1 - i] = data[i][j]
                else:
                    new_data[m - 1 - j][i] = data[i][j]
    return new_data
def analyze_log(check_data):
    for c in change_log:
        if c < 3:
            check_data = flip(check_data, c)
        else:
            check_data = rotate(check_data, c)
    return check_data
def rotate_data():
    new_data = []
    for i in range(0, 4, 2):
        for j in range(0, 4, 2):
            col = []
            if check_data[i][j][0] == check_data[i][j + 1][0]:
                dir_col = -1 if check_data[i][j][0] > check_data[i + 1][j][0] else 1
                for k in range(check_data[i][j][0], check_data[i + 1][j][0] + dir_col, dir_col):
                    row = []
                    dir_row = -1 if check_data[i][j][1] > check_data[i][j + 1][1] else 1
                    for l in range(check_data[i][j][1], check_data[i][j + 1][1] + dir_row, dir_row):
                        row.append(data[k][l])
                    col.append(row)
            else:
                dir_col = -1 if check_data[i][j][1] > check_data[i + 1][j][1] else 1
                for k in range(check_data[i][j][1], check_data[i + 1][j][1] + dir_col, dir_col):
                    row = []
                    dir_row = -1 if check_data[i][j][0] > check_data[i][j + 1][0] else 1
                    for l in range(check_data[i][j][0], check_data[i][j + 1][0] + dir_row, dir_row):
                        row.append(data[l][k])
                    col.append(row)
            new_data.append(col)
    return new_data
def print_data(data):
    if n < 4 or m < 4:
        for d in data:
            print(*d)
    else:
        for i in range(0, 4, 2):
            for j in range(len(data[i])):
                print(*data[i][j], end=' ')
                print(*data[i + 1][j])
check_data = analyze_log(check_data)
if n < 4 or m < 4:
    print_data(check_data)
else:
    print_data(rotate_data())
