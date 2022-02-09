import sys
map_data = [[0] * 6 for _ in range(6)]
map_data[2][2] = map_data[3][3] = 2
map_data[2][3] = map_data[3][2] = 1
check_pos = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
def check(turn, x, y):
    for check_dir in check_pos:
        nx = x + check_dir[0]
        ny = y + check_dir[1]
        count = 0
        can_flip = False
        while 0 <= nx < 6 and 0 <= ny < 6:
            if map_data[nx][ny] == 0:
                break
            elif map_data[nx][ny] == turn:
                can_flip = True
                break
            nx += check_dir[0]
            ny += check_dir[1]
            count += 1
        if can_flip:
            nx = x
            ny = y
            for _ in range(count + 1):
                map_data[nx][ny] = turn
                nx += check_dir[0]
                ny += check_dir[1]
player = 1
for _ in range(int(sys.stdin.readline().rstrip())):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    x, y = x - 1, y - 1
    check(player, x, y)
    player = 1 if player == 2 else 2
black = white = 0
for r in map_data:
    for c in r:
        if c == 1:
            print('B', end='')
            black += 1
        elif c == 2:
            print('W', end='')
            white += 1
        else:
            print('.', end='')
    print()
print(f'{"Black" if black > white else "White"}')