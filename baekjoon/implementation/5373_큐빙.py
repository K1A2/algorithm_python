import sys
input = sys.stdin.readline
init = lambda x: [[x] * 3 for _ in range(3)]
dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
def rotate_90(data, dir):
    for _ in range(3 if dir == 1 else 1):
        new_data = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                new_data[j][2 - i] = data[i][j]
        data = new_data
    return data

def change_left(up, down, front, back, left, dir):
    for _ in range(3 if dir == '-' else 1):
        left = rotate_90(left, 0)
        save = [front[0][0], front[1][0], front[2][0]]
        front[0][0], front[1][0], front[2][0] = up[0][0], up[1][0], up[2][0]
        down[2][2], down[1][2], down[0][2], save = save[0], save[1], save[2], [down[2][2], down[1][2], down[0][2]]
        back[2][2], back[1][2], back[0][2], save = save[0], save[1], save[2], [back[2][2], back[1][2], back[0][2]]
        up[0][0], up[1][0], up[2][0] = save[0], save[1], save[2]
    return up, down, front, back, left

def change_right(up, down, front, back, right, dir):
    for _ in range(3 if dir == '-' else 1):
        right = rotate_90(right, 0)
        save = [back[0][0], back[1][0], back[2][0]]
        back[0][0], back[1][0], back[2][0] = up[2][2], up[1][2], up[0][2]
        down[0][0], down[1][0], down[2][0], save = save[0], save[1], save[2], [down[0][0], down[1][0], down[2][0]]
        front[2][2], front[1][2], front[0][2], save = save[0], save[1], save[2], [front[2][2], front[1][2], front[0][2]]
        up[2][2], up[1][2], up[0][2] = save[0], save[1], save[2]
    return up, down, front, back, right

def change_down(down, front, back, left, right, dir):
    for _ in range(3 if dir == '-' else 1):
        down = rotate_90(down, 0)
        save = [right[2][2], right[1][2], right[0][2]]
        right[2][2], right[1][2], right[0][2] = front[2]
        back[2], save = save, back[2]
        left[0][0], left[1][0], left[2][0], save = save[0], save[1], save[2], [left[0][0], left[1][0], left[2][0]]
        front[2] = save
    return down, front, back, left, right

def change_up(up, front, back, left, right, dir):
    for _ in range(3 if dir == '-' else 1):
        up = rotate_90(up, 0)
        save = [left[0][2], left[1][2], left[2][2]]
        left[0][2], left[1][2], left[2][2] = front[0]
        back[0], save = save, back[0]
        right[0][0], right[1][0], right[2][0], save = save[2], save[1], save[0], [right[0][0], right[1][0], right[2][0]]
        front[0] = [save[2], save[1], save[0]]
    return up, front, back, left, right

def change_back(up, down, back, left, right, dir):
    for _ in range(3 if dir == '-' else 1):
        back = rotate_90(back, 0)
        save = up[0]
        left[0], save = save, left[0]
        down[0], save = save, down[0]
        right[0], save = save, right[0]
        up[0] = save
    return up, down, back, left, right

def change_front(up, down, front, left, right, dir):
    for _ in range(3 if dir == '-' else 1):
        front = rotate_90(front, 0)
        save = up[2]
        save, right[2] = right[2], save
        save, down[2] = down[2], save
        save, left[2] = left[2], save
        up[2] = save
    return up, down, front, left, right

for _ in range(int(input())):
    up, down, front, back, left, right = init('w'), init('y'), init('r'), init('o'), init('g'), init('b')
    n = int(input())
    log = input().rstrip().split()
    for i in log:
        if i[0] == 'R':
            up, down, front, back, right = change_right(up, down, front, back, right, i[1])
        elif i[0] == 'L':
            up, down, front, back, left = change_left(up, down, front, back, left, i[1])
        elif i[0] == 'U':
            up, front, back, left, right = change_up(up, front, back, left, right, i[1])
        elif i[0] == 'D':
            down, front, back, left, right = change_down(down, front, back, left, right, i[1])
        elif i[0] == 'F':
            up, down, front, left, right = change_front(up, down, front, left, right, i[1])
        elif i[0] == 'B':
            up, down, back, left, right = change_back(up, down, back, left, right, i[1])
    for d in up:
        print(''.join(d))
