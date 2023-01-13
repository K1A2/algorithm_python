import sys
input = sys.stdin.readline
def parse_eq(a):
    new_a = []
    for i in range(len(a)):
        if a[i] == '+' or a[i] == '-':
            continue
        new_data = []
        num_idx = 1
        if a[i][0] == '-':
            if i > 0 and a[i - 1] == '-':
                new_data.append('+')
            else:
                new_data.append('-')
        else:
            if i > 0 and a[i - 1] == '-':
                new_data.append('-')
            else:
                new_data.append('+')
            if a[i][0] != '+':
                num_idx = 0
        if a[i][-1].isdigit():
            number = int(a[i][num_idx:])
            new_data.append(number)
        elif a[i][-1] == 'x' or a[i][-1] == 'y':
            if a[i][num_idx].isdigit():
                number = int(a[i][num_idx:-1])
            else:
                number = 1
            new_data.append(number)
            new_data.append(a[i][-1])
        new_a.append(new_data)
    return new_a

def sep_num(left, right):
    n_left = []
    n_right = []
    for l in left:
        if isinstance(l[-1], int):
            if l[0] == '-':
                l[0] = '+'
            else:
                l[0] = '-'
            n_right.append(l)
        else:
            n_left.append(l)
    for r in right:
        if isinstance(r[-1], int):
            n_right.append(r)
        else:
            if r[0] == '-':
                r[0] = '+'
            else:
                r[0] = '-'
            n_left.append(r)
    if not len(n_left):
        n_left.append(['+', 0])
    if not len(n_right):
        n_right.append(['+', 0])
    return n_left, n_right

def eq_sum(data):
    if isinstance(data[0][-1], int):
        number = 0
        for i in data:
            if i[0] == '+':
                number += i[1]
            else:
                number -= i[1]
        return [[number]]
    x_num = 0
    y_num = 0
    for i in data:
        if i[-1] == 'x':
            if i[0] == '+':
                x_num += i[1]
            else:
                x_num -= i[1]
        else:
            if i[0] == '+':
                y_num += i[1]
            else:
                y_num -= i[1]
    new_data = []
    if x_num:
        new_data.append([x_num, 'x'])
    if y_num:
        new_data.append([y_num, 'y'])
    if len(new_data) == 0:
        new_data.append([0])
    return new_data

def eq_gop(left, right, a):
    for l in left:
        l[0] *= a
    for l in right:
        l[0] *= a
    return left, right

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
    return a

def print_answer(down, up):
    if abs(down) == 1:
        a = str(up // down)
    else:
        if down < 0:
            down *= -1
            up *= -1
        a = str(up) + '/' + str(down)
    print(a)

n = int(input())
for k in range(n):
    linear1_left, linear1_right = input().rstrip().split('=')
    linear2_left, linear2_right = input().rstrip().split('=')

    linear1_left = parse_eq(linear1_left.split())
    linear1_right = parse_eq(linear1_right.split())
    linear2_left = parse_eq(linear2_left.split())
    linear2_right = parse_eq(linear2_right.split())

    linear1_left, linear1_right = sep_num(linear1_left, linear1_right)
    linear2_left, linear2_right = sep_num(linear2_left, linear2_right)

    linear1_left = eq_sum(linear1_left)
    linear1_right = eq_sum(linear1_right)
    linear2_left = eq_sum(linear2_left)
    linear2_right = eq_sum(linear2_right)

    if len(linear1_left) < len(linear2_left):
        linear1_left, linear2_left = linear2_left, linear1_left
        linear1_right, linear2_right = linear2_right, linear1_right

    if len(linear1_left) == 2 and len(linear2_left) == 2:
        ax1 = linear2_left[0][0]
        ax2 = -linear1_left[0][0]
        linear1_left, linear1_right = eq_gop(linear1_left, linear1_right, ax1)
        linear2_left, linear2_right = eq_gop(linear2_left, linear2_right, ax2)
        new_right = [[linear1_right[0][0] + linear2_right[0][0]]]
        new_left = []
        for i in range(2):
            a = linear1_left[i][0] + linear2_left[i][0]
            if a:
                new_left.append([a, linear1_left[i][1]])
        if new_left:
            y_gcd = gcd(new_left[0][0], new_right[0][0])
            y_up = new_right[0][0] // y_gcd
            y_down = new_left[0][0] // y_gcd

            ay1 = linear2_left[1][0]
            ay2 = -linear1_left[1][0]
            linear1_left, linear1_right = eq_gop(linear1_left, linear1_right, ay1)
            linear2_left, linear2_right = eq_gop(linear2_left, linear2_right, ay2)
            new_right = [[linear1_right[0][0] + linear2_right[0][0]]]
            new_left = []
            for i in range(2):
                a = linear1_left[i][0] + linear2_left[i][0]
                if a:
                    new_left.append([a, linear1_left[i][1]])
            x_gcd = gcd(new_left[0][0], new_right[0][0])
            x_up = new_right[0][0] // x_gcd
            x_down = new_left[0][0] // x_gcd

            print_answer(x_down, x_up)
            print_answer(y_down, y_up)
        else:
            print('don\'t know')
            print('don\'t know')
    elif len(linear1_left) == 2 and len(linear2_left) == 1:
        if linear2_left[0][0] == 0:
            print('don\'t know')
            print('don\'t know')
        else:
            x = y = 0
            n_gcd = gcd(linear2_left[0][0], linear2_right[0][0])
            n_up = linear2_right[0][0] // n_gcd
            n_down = linear2_left[0][0] // n_gcd

            if n_down < 0:
                n_up *= -1
                n_down *= -1

            if linear2_left[0][1] == 'x':
                x_up = n_up
                x_down = n_down
                if x_down != 1:
                    linear1_left[1][0] *= x_down
                    linear1_right[0][0] *= x_down
                x_gop = x_up * linear1_left[0][0]
                del linear1_left[0]
                linear1_right[0][0] -= x_gop
                y_gcd = gcd(linear1_left[0][0], linear1_right[0][0])
                y_up = linear1_right[0][0] // y_gcd
                y_down = linear1_left[0][0] // y_gcd
            else:
                y_up = n_up
                y_down = n_down
                if y_down != 1:
                    linear1_left[0][0] *= y_down
                    linear1_right[0][0] *= y_down
                y_gop = y_up * linear1_left[1][0]
                del linear1_left[1]
                linear1_right[0][0] -= y_gop
                x_gcd = gcd(linear1_left[0][0], linear1_right[0][0])
                x_up = linear1_right[0][0] // x_gcd
                x_down = linear1_left[0][0] // x_gcd
            print_answer(x_down, x_up)
            print_answer(y_down, y_up)
    else:
        if linear1_left[0][0] != 0 and linear2_left[0][0] != 0:
            if linear1_left[0][1] == linear2_left[0][1]:
                if linear1_right[0][0] == linear2_right[0][0]:
                    if linear1_left[0][1] == 'x':
                        print(linear1_right[0][0])
                        print('don\'t know')
                    else:
                        print('don\'t know')
                        print(linear1_right[0][0])
                else:
                    print('don\'t know')
                    print('don\'t know')
            else:
                if linear2_left[0][1] == 'x':
                    linear1_left, linear2_left = linear2_left, linear1_left
                    linear1_right, linear2_right = linear2_right, linear1_right
                x_gcd = gcd(linear1_left[0][0], linear1_right[0][0])
                x_up = linear1_right[0][0] // x_gcd
                x_down = linear1_left[0][0] // x_gcd

                y_gcd = gcd(linear2_left[0][0], linear2_right[0][0])
                y_up = linear2_right[0][0] // y_gcd
                y_down = linear2_left[0][0] // y_gcd

                print_answer(x_down, x_up)
                print_answer(y_down, y_up)
        elif linear1_left[0][0] == 0 and linear2_left[0][0] == 0:
            print('don\'t know')
            print('don\'t know')
        else:
            if linear1_left[0][0] == 0:
                linear1_left, linear2_left = linear2_left, linear1_left
                linear1_right, linear2_right = linear2_right, linear1_right
            if linear2_right[0][0] != 0:
                print('don\'t know')
                print('don\'t know')
            else:
                n_gcd = gcd(linear1_left[0][0], linear1_right[0][0])
                n_up = linear1_right[0][0] // n_gcd
                n_down = linear1_left[0][0] // n_gcd
                if linear1_left[0][1] == 'x':
                    print_answer(n_down, n_up)
                    print('don\'t know')
                else:
                    print('don\'t know')
                    print_answer(n_down, n_up)

    if k != n - 1:
        input()
        print()
