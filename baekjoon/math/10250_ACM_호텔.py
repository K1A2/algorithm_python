for _ in range(int(input())):
    h, w, n = list(map(int, input().split()))
    if n % h != 0:
        print('%d%02d' % (n % h, n // h + 1))
    else:
        print('%d%02d' % (h, n // h))