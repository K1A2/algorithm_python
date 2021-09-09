x, y = map(int, input().split())
checked = [[False for _ in range(y)] for _ in range(x)]
character = list(map(int, input().split()))
pos = [character[0], character[1]]
see = character[2]

checked[pos[0]][pos[1]] = True

map_data = []
for _ in range(x):
    map_data.append(list(map(int, input().split())))

turn = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cant = 0
count = 1
while True:
    if cant == 4:
        cant = 0
        pos = [pos[0] + 1, pos[1]]
        if checked[pos[0]][pos[1]] or map_data[pos[0]][pos[1]] == 1:
            break
        count += 1
        checked[pos[0]][pos[1]] = True
        continue
    see -= 1
    if see < 0:
        see = 3
    check_y, check_x = pos[0] + turn[see][0], pos[1] + turn[see][1]

    if checked[check_y][check_x] or map_data[check_y][check_x] == 1:
        cant += 1
        continue
    count += 1
    checked[check_y][check_x] = True
    pos = [check_y, check_x]
    cant = 0
print(count)