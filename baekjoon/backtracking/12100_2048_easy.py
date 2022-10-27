import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = [list(map(int, input().rstrip().split())) for _ in range(n)]

def left():
    data_new = [i[:] for i in data]
    for x in range(n):
        y_less = 0
        y_now = 1
        while y_now < n:
            if not data_new[x][y_now]:
                y_now += 1
                continue
            if y_less == y_now:
                y_now += 1
            if data_new[x][y_less] == data_new[x][y_now]:
                data_new[x][y_less] *= 2
                data_new[x][y_now] = 0
                y_less += 1
            else:
                if data_new[x][y_less]:
                    if y_less + 1 != y_now:
                        data_new[x][y_less + 1] = data_new[x][y_now]
                        data_new[x][y_now] = 0
                    y_less += 1
                else:
                    data_new[x][y_less] = data_new[x][y_now]
                    data_new[x][y_now] = 0
            y_now += 1
    return data_new

def right():
    data_new = [i[:] for i in data]
    for x in range(n):
        y_max = n - 1
        y_now = n - 2
        while y_now >= 0:
            if not data_new[x][y_now]:
                y_now -= 1
                continue
            if y_max == y_now:
                y_now -= 1
            if data_new[x][y_max] == data_new[x][y_now]:
                data_new[x][y_max] *= 2
                data_new[x][y_now] = 0
                y_max -= 1
            else:
                if data_new[x][y_max]:
                    if y_max - 1 != y_now:
                        data_new[x][y_max - 1] = data_new[x][y_now]
                        data_new[x][y_now] = 0
                    y_max -= 1
                else:
                    data_new[x][y_max] = data_new[x][y_now]
                    data_new[x][y_now] = 0
            y_now -= 1
    return data_new

def up():
    data_new = [i[:] for i in data]
    for y in range(n):
        x_less = 0
        x_now = 1
        while x_now < n:
            if not data_new[x_now][y]:
                x_now += 1
                continue
            if x_less == x_now:
                x_now += 1
            if data_new[x_less][y] == data_new[x_now][y]:
                data_new[x_less][y] *= 2
                data_new[x_now][y] = 0
                x_less += 1
            else:
                if data_new[x_less][y]:
                    if x_less + 1 != x_now:
                        data_new[x_less + 1][y] = data_new[x_now][y]
                        data_new[x_now][y] = 0
                    x_less += 1
                else:
                    data_new[x_less][y] = data_new[x_now][y]
                    data_new[x_now][y] = 0
            x_now += 1
    return data_new

def down():
    pass

def print_board(d):
    for i in d:
        print(' '.join(list(map(str, i))))
    print()

print_board(left())
print_board(right())
print_board(up())
