k = 100001
prime = [1] * k
prime[0] = prime[1] = 0
for i in range(2, int(k ** 0.5)):
    for p in range(i * 2, k, i):
        prime[p] = 0

for _ in range(int(input())):
    n = int(input())

    p = 2
    while n > 1:
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        if count:
            print(p, count)
        for next_p in range(p + 1, k):
            if prime[next_p]:
                p = next_p
                break
