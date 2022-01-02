for _ in range(int(input())):
    k, n = int(input()), int(input())
    s = 1
    k += 1
    for i in range(1, n):
        com = 1
        com2 = 1
        for y in range(i):
            com *= k - y
            com2 *= (y + 1)
        s += com // com2
        k += 1
    print(s)