def divide_arr_idx(from_x, from_y, to_x, to_y):
    t = (to_x - from_x + 1) // 2
    mid_x = t + from_x
    mid_y = t + from_y
    return (from_x, from_y, mid_x - 1, mid_y - 1), (mid_x, from_y, to_x, mid_y - 1), (mid_x, mid_y, to_x, to_y), (
    from_x, mid_y, mid_x - 1, to_y)


def quad(zero, one, arr, from_x, from_y, to_x, to_y):
    key = arr[from_x][from_y]
    is_type = -1
    if key:
        is_type = 1
    else:
        is_type = 0
    for x in range(from_x, to_x + 1):
        for y in range(from_y, to_y + 1):
            if arr[x][y] != key:
                is_type = -1
                break
    if is_type == -1:
        for nxy in divide_arr_idx(from_x, from_y, to_x, to_y):
            is_not = False
            for xy in nxy:
                if xy < 0 or len(arr) <= xy:
                    is_not = True
                    break
            if is_not: continue
            zero, one = quad(zero, one, arr, nxy[0], nxy[1], nxy[2], nxy[3])
    elif is_type:
        return zero, one + 1
    else:
        return zero + 1, one
    return zero, one

def solution(arr):
    zero = one = 0
    zero, one = quad(zero, one, arr, 0, 0, len(arr) - 1, len(arr) - 1)
    return [zero, one]

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]) == [4, 9])
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],
                [0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]) == [10, 15])
print(solution([[1]]) == [0, 1])
print(solution([[0, 0], [0, 0]]) == [1, 0])