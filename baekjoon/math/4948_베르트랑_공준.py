while True:
    num = int(input())
    if num == 0:
        break
    a, b = num + 1, num * 2
    check = [False, False] + [True] * (b - 1)
    s = []
    for i in range(2, b + 1):
        if check[i]:
            if a <= i:
                s.append(i)
            for j in range(2 * i, b + 1, i):
                check[j] = False
    print(len(s))