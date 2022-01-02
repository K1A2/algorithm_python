while True:
    l = list(map(int, input().split()))
    if l[0] == 0:
        break
    larger = max(l)
    l.remove(larger)
    if larger ** 2 == l[0] ** 2 + l[1] ** 2:
        print("right")
    else:
        print("wrong")