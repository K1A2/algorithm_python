n, k = map(int, input().split())
prime = [1] * (n + 1)
prime[0] = prime[1] = 0
count = 0
for p in range(2, n + 1):
    if prime[p] == 0:
        continue
    for i in range(p, n + 1, p):
        if prime[i] == 0:
            continue
        prime[i] = 0
        count += 1
        if count == k:
            print(i)
            exit()
