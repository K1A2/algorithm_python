m = 1000000
primes = [i for i in range(m + 1)]
for i in range(2, m // 2):
    for j in range(i * 2, m + 1, i):
        primes[j] = 0
for _ in range(int(input())):
    num = int(input())
    count = 0
    for i in range(2, num // 2 + 1):
        if primes[i] and primes[num - i]:
            count += 1
    print(count)