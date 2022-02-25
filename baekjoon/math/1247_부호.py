for _ in range(3):
    a = 0
    for _ in range(int(input())):
        a += int(input())
    if a == 0:
        print(0)
    elif a > 0:
        print('+')
    else:
        print('-')