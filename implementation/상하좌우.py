n = int(input())
move = input().split()

pos = [1, 1]
for m in move:
    moving = [0, 0]
    if m == 'R':
        moving = [0, 1]
    elif m == 'L':
        moving = [0, -1]
    elif m == 'U':
        moving = [-1, 0]
    elif m == 'D':
        moving = [1, 0]
    if pos[0] + moving[0] > 0 and pos[1] + moving[1] > 0:
        pos = [pos[i] + moving[i] for i in range(2)]
print(pos)