prime = [1] * 1299710
for i in range(2, int(1299711 ** 0.5)):
    for p in range(i * 2, 1299710, i):
        prime[p] = 0
prime[0] = prime[1] = 0
for _ in range(int(input())):
    n = int(input())
    if prime[n]:
        print(0)
        continue
    l = r = n
    while 1:
        l -= 1
        if prime[l]:
            break
    while 1:
        r += 1
        if prime[r]:
            break
    print(r - l)
