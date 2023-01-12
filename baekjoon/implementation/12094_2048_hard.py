import sys
input = sys.stdin.readline
n = int(input().rstrip())
data = [list(map(int, input().rstrip().split())) for _ in range(n)]

import time
start = time.time()

def left(data):
    data_new = [i[:] for i in data]
    max_number = -1
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
                if max_number < data_new[x][y_less]: max_number = data_new[x][y_less]
                y_less += 1
            else:
                if data_new[x][y_less]:
                    if y_less + 1 != y_now:
                        data_new[x][y_less + 1] = data_new[x][y_now]
                        data_new[x][y_now] = 0
                        if max_number < data_new[x][y_less + 1]: max_number = data_new[x][y_less + 1]
                    y_less += 1
                else:
                    data_new[x][y_less] = data_new[x][y_now]
                    data_new[x][y_now] = 0
                    if max_number < data_new[x][y_less]: max_number = data_new[x][y_less]
            y_now += 1
    return data_new, max_number

def right(data):
    data_new = [i[:] for i in data]
    max_number = -1
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
                if max_number < data_new[x][y_max]: max_number = data_new[x][y_max]
                y_max -= 1
            else:
                if data_new[x][y_max]:
                    if y_max - 1 != y_now:
                        data_new[x][y_max - 1] = data_new[x][y_now]
                        data_new[x][y_now] = 0
                        if max_number < data_new[x][y_max - 1]: max_number = data_new[x][y_max - 1]
                    y_max -= 1
                else:
                    data_new[x][y_max] = data_new[x][y_now]
                    data_new[x][y_now] = 0
                    if max_number < data_new[x][y_max]: max_number = data_new[x][y_max]
            y_now -= 1
    return data_new, max_number

def up(data):
    data_new = [i[:] for i in data]
    max_number = -1
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
                if max_number < data_new[x_less][y]: max_number = data_new[x_less][y]
                x_less += 1
            else:
                if data_new[x_less][y]:
                    if x_less + 1 != x_now:
                        data_new[x_less + 1][y] = data_new[x_now][y]
                        data_new[x_now][y] = 0
                        if max_number < data_new[x_less + 1][y]: max_number = data_new[x_less + 1][y]
                    x_less += 1
                else:
                    data_new[x_less][y] = data_new[x_now][y]
                    data_new[x_now][y] = 0
                    if max_number < data_new[x_less][y]: max_number = data_new[x_less][y]
            x_now += 1
    return data_new, max_number

def down(data):
    data_new = [i[:] for i in data]
    max_number = -1
    for y in range(n):
        x_max = n - 1
        x_now = n - 2
        while x_now >= 0:
            if not data_new[x_now][y]:
                x_now -= 1
                continue
            if x_max == x_now:
                x_now -= 1
            if data_new[x_max][y] == data_new[x_now][y]:
                data_new[x_max][y] *= 2
                data_new[x_now][y] = 0
                if max_number < data_new[x_max][y]: max_number = data_new[x_max][y]
                x_max -= 1
            else:
                if data_new[x_max][y]:
                    if x_max - 1 != x_now:
                        data_new[x_max - 1][y] = data_new[x_now][y]
                        data_new[x_now][y] = 0
                        if max_number < data_new[x_max - 1][y]: max_number = data_new[x_max - 1][y]
                    x_max -= 1
                else:
                    data_new[x_max][y] = data_new[x_now][y]
                    data_new[x_now][y] = 0
                    if max_number < data_new[x_max][y]: max_number = data_new[x_max][y]
            x_now -= 1
    return data_new, max_number

def backtracking(depth, data, max_number, least, res):
    if depth == 10:
        res = max(res, max_number)
        s = res
        while depth > 0:
            depth -= 1
            least[depth] = s
            s //= 2
        return res, least
    for func in [left, right, up, down]:
        new_data, max_number = func(data)
        if max_number == -1 or max_number <= least[depth]:
            continue
        res, least = backtracking(depth + 1, new_data, max_number, least, res)
    return res, least

if n > 1:
    init_max = max([max(d) for d in data])
    init_least = [0] * 10
    print(backtracking(0, data, 0, init_least, 0)[0])
else:
    print(data[0][0])
# end = time.time()
# print(end - start, 'sec')