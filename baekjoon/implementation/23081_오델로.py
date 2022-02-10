n = int(input())
data = [list(input()) for _ in range(n)]
res = [0, 0]
check_pos = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
for x in range(n):
    for y in range(n):
        if data[x][y] == '.':
            count_all = 0
            for check_dir in check_pos:
                nx = x + check_dir[0]
                ny = y + check_dir[1]
                count = 0
                is_possible = False
                while 0 <= nx < n and 0 <= ny < n:
                    if data[nx][ny] == '.':
                        break
                    elif data[nx][ny] == 'B':
                        is_possible = True
                        break
                    nx += check_dir[0]
                    ny += check_dir[1]
                    count += 1
                if is_possible and count:
                    count_all += count
            if count_all and res[1] < count_all:
                res = [[y, x], count_all]
if res != [0, 0]:
    print(' '.join([str(i) for i in res[0]]) + '\n' + str(res[1]))
else:
    print('PASS')