for _ in range(int(input())):
    num = int(input())
    mook = num // 2
    k = 0
    a = [mook, mook]
    isA = True
    while True:
        for i in a:
            for l in range(2, i // 2 + 1):
                if i % l == 0:
                    isA = False
                    break
            if not isA:
                break
        if isA:
            print(a[0], a[1])
            break
        else:
            k += 1
            a = [mook - k, mook + k]
            isA = True