n, m, sx, sy, k = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(n)]
dice = [0, 0, 0, 0, 0, 0] # top, back, right, left, front, bottom
for p in map(int, input().split()):
    if p == 1: # e
        nsx = sx
        nsy = sy + 1
        if not (0 <= nsx < n and 0 <= nsy < m):
            continue
        new_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif p == 2: # w
        nsx = sx
        nsy = sy - 1
        if not (0 <= nsx < n and 0 <= nsy < m):
            continue
        new_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif p == 3: # n
        nsx = sx - 1
        nsy = sy
        if not (0 <= nsx < n and 0 <= nsy < m):
            continue
        new_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif p == 4: # s
        nsx = sx + 1
        nsy = sy
        if not (0 <= nsx < n and 0 <= nsy < m):
            continue
        new_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    if map_data[nsx][nsy] == 0:
        map_data[nsx][nsy] = new_dice[5]
    else:
        new_dice[5] = map_data[nsx][nsy]
        map_data[nsx][nsy] = 0
    sx = nsx
    sy = nsy
    print(new_dice[0])
    dice = new_dice
    # print(dice, sx, sy)
