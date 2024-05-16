prime = [1] * 150000
for i in range(2, int(150000 ** 0.5)):
    for p in range(i * 2, 150000, i):
        prime[p] = 0
prime[0] = prime[1] = 0

for _ in range(int(input())):
    n = int(input())
    flag = 0
    for i in range(n, 150000):
        if prime[i]: continue
        if flag: break
        for p in range(2, int(i ** 0.5) + 1):
            if not prime[p]:
                continue
            if prime[i // p] and i // p != p and i // p * p == i:
                print(i)
                flag = 1
                break
