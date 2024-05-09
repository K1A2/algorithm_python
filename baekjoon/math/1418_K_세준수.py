n, k = int(input()), int(input())
prime = [1] * (n + 1)
prime[0] = prime[1] = 0
for i in range(2, int((n + 1) ** 1/2)):
    for j in range(i * 2, n + 1, i):
        prime[j] = 0

ans = [1] * (n + 1)
for i in range(2, n + 1):
    if prime[i] and i > k:
        for j in range(i, n + 1, i):
            ans[j] = 0
print(sum(ans) - 1)
