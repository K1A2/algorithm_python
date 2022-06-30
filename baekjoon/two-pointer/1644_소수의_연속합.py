n = int(input())
primes = [i for i in range(n + 1)]
for i in range(2, (n + 1) // 2 + 1):
    if primes[i]:
        for j in range(i * 2, n + 1, i):
            primes[j] = 0
count = in_sum = 0
end = 2
for start in range(2, n + 1):
    if primes[start]:
        while in_sum < n and end <= n:
            if primes[end]: in_sum += primes[end]
            end += 1
        if in_sum == n:
            count += 1
        in_sum -= primes[start]
print(count)