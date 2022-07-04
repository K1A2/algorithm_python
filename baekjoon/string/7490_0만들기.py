def find(now, to, cal_str, cal_str_no_space):
    if now > to:
        if not eval(cal_str_no_space):
            print(cal_str)
        return
    if now == 1:
        find(now + 1, to, cal_str + f'{now}', cal_str_no_space + f'+{now}')
    else:
        find(now + 1, to, cal_str + f' {now}', cal_str_no_space + f'{now}')
        find(now + 1, to, cal_str + f'+{now}', cal_str_no_space + f'+{now}')
        find(now + 1, to, cal_str + f'-{now}', cal_str_no_space + f'-{now}')

for _ in range(int(input())):
    find(1, int(input()), '', '')
    print()