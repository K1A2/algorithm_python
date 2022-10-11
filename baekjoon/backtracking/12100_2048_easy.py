import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = [list(map(int, input().rstrip().split())) for _ in range(n)]

def left(data):
    new_data = []
    for i in data:
        new_row = i[:]
        last_zero_idx = 0
        for j in range(1, n):
            if new_row[j]:
                if new_row[last_zero_idx] == new_row[j]:
                    new_row[last_zero_idx] *= 2
                    for k in range(last_zero_idx + 1, j + 1): new_row[k] = 0
                    last_zero_idx += 1
                else:
                    if not new_row[last_zero_idx]:
                        new_row[last_zero_idx] = new_row[j]
                        for k in range(last_zero_idx + 1, j + 1): new_row[k] = 0
                    else:
                        last_zero_idx += 1
        new_data.append(new_row)
    return new_data

def right(data):
    new_data = []
    for i in data:
        new_row = i[:]
        last_zero_idx = n - 1
        for j in range(n - 2, -1, -1):
            if new_row[j]:
                if new_row[last_zero_idx] == new_row[j]:
                    new_row[last_zero_idx] *= 2
                    for k in range(j, last_zero_idx): new_row[k] = 0
                    last_zero_idx -= 1
                else:
                    if not new_row[last_zero_idx]:
                        new_row[last_zero_idx] = new_row[j]
                        for k in range(j, last_zero_idx): new_row[k] = 0
                    else:
                        last_zero_idx -= 1
        new_data.append(new_row)
    return new_data

def up(data):
    new_data = []
    for i in data:
        new_data.append(i[:])
    for i in range(n):
        last_zero_idx = 0
        for j in range(1, n):
            if new_data[j][i]:
                if new_data[last_zero_idx][i] == new_data[j][i]:
                    new_data[last_zero_idx][i] *= 2
                    for k in range(last_zero_idx + 1, j + 1): new_data[k][i] = 0
                    last_zero_idx += 1
                else:
                    if not new_data[last_zero_idx][i]:
                        new_data[last_zero_idx][i] = new_data[j][i]
                        for k in range(last_zero_idx + 1, j + 1): new_data[k][i] = 0
                    else:
                        last_zero_idx += 1
    return new_data

def down(data):
    new_data = []
    for i in data:
        new_data.append(i[:])
    for i in range(n):
        last_zero_idx = n - 1
        for j in range(n - 2, -1, -1):
            if new_data[j][i]:
                if new_data[last_zero_idx][i] == new_data[j][i]:
                    new_data[last_zero_idx][i] *= 2
                    for k in range(j, last_zero_idx): new_data[k][i] = 0
                    last_zero_idx -= 1
                else:
                    if not new_data[last_zero_idx][i]:
                        new_data[last_zero_idx][i] = new_data[j][i]
                        for k in range(j, last_zero_idx): new_data[k][i] = 0
                    else:
                        last_zero_idx -= 1
    return new_data

# def backtracking(data_copy, depth, ans):
#     if depth == 5:
#         return max((ans, max([max(i) for i in data_copy])))


# print(backtracking((data)))

print(left(data))
print(right(data))
print(up(data))
print(down(data))
