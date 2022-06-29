m = 1000000
primes = [i for i in range(m + 1)]
for i in range(2, m // 2):
    for j in range(i * 2, m + 1, i):
        primes[j] = 0
while True:
    num = int(input())
    if not num:
        break
    find = 0
    for i in range(2, num // 2 + 1):
        if primes[i] and primes[num - i]:
            find = 1
            print(f'{num} = {i} + {num - i}')
            break
    if not find:
        print("Goldbach's conjecture is wrong.")