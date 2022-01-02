num = int(input())
o = num // 5
if num % 5 == 0:
    print(o)
else:
    is_d = False
    for i in range(o, 0, -1):
        t = num - 5 * i
        if t % 3 == 0:
            print(t // 3 + i)
            is_d = True
            break
    if not is_d:
        if num % 3 == 0:
            print(num // 3)
        else:
            print(-1)