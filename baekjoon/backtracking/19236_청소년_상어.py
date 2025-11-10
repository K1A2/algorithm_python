data = []
fish = [[] for _ in range(17)]
for j in range(4):
    a = list(map(int, input().split()))
    l = []
    for en, i in enumerate(range(0, 8, 2)):
        l.append(a[i])
        fish[a[i]] = [(j, en), a[i + 1] - 1]
    data.append(l)

move = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
eat = data[0][0]
shark = [(0, 0), fish[data[0][0]][1]]
fish[data[0][0]] = -1
data[0][0] = -1

ans = 0

def backtracking(fish_num, eat):
    global ans, shark

    if fish_num == 'shark':
        move_able = []
        position, direction = shark
        idx = 1
        while 1:
            nx = position[0] + move[direction][0] * idx
            ny = position[1] + move[direction][1] * idx
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                break
            if data[nx][ny] == 0:
                idx += 1
                continue
            move_able.append((nx, ny))
            idx += 1
        if len(move_able) == 0:
            ans = max(ans, eat)
            return
        for nx, ny in move_able:
            eated_fish = data[nx][ny]
            eated_fish_info = fish[eated_fish]
            eat += eated_fish
            fish[eated_fish] = -1
            data[position[0]][position[1]] = 0
            data[nx][ny] = -1
            shark = [(nx, ny), eated_fish_info[1]]
            nex_fish = 0
            while 1:
                nex_fish += 1
                if nex_fish > 16:
                    ans = max(ans, eat)
                    return
                if fish[nex_fish] != -1:
                    break
            backtracking(nex_fish, eat)
            eat -= eated_fish
            fish[eated_fish] = eated_fish_info
            data[position[0]][position[1]] = -1
            data[nx][ny] = eated_fish
            shark = [position, direction]
    else:
        position, direction = fish[fish_num]
        n_direction = direction
        while 1:
            nx = position[0] + move[n_direction][0]
            ny = position[1] + move[n_direction][1]
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or data[nx][ny] == -1:
                n_direction = (n_direction + 1) % 8
            else:
                break
        if data[nx][ny] == 0:
            data[position[0]][position[1]] = 0
            data[nx][ny] = fish_num
            fish[fish_num] = [(nx, ny), n_direction]
            nex_fish = fish_num
            while 1:
                nex_fish += 1
                if nex_fish > 16:
                    nex_fish = 'shark'
                    break
                if fish[nex_fish] != -1:
                    break
            backtracking(nex_fish, eat)
            fish[fish_num] = (position, direction)
            data[position[0]][position[1]] = fish_num
            data[nx][ny] = 0
        else:
            other_fish_num = data[nx][ny]
            other_fish_info = fish[other_fish_num]

            data[position[0]][position[1]] = other_fish_num
            data[nx][ny] = fish_num
            fish[other_fish_num] = [(position[0], position[1]), other_fish_info[1]]
            fish[fish_num] = [(nx, ny), n_direction]
            nex_fish = fish_num
            while 1:
                nex_fish += 1
                if nex_fish > 16:
                    nex_fish = 'shark'
                    break
                if fish[nex_fish] != -1:
                    break
            backtracking(nex_fish, eat)
            fish[fish_num] = (position, direction)
            fish[other_fish_num] = other_fish_info
            data[position[0]][position[1]] = fish_num
            data[nx][ny] = other_fish_num

for i in range(1, 17):
    stat_fish = i
    if fish[i] != -1: break
backtracking(stat_fish, eat)
print(ans)
