n = int(input())
data = list(map(int, input().split()))
k = 1000001
prime = [1] * k
prime[0] = prime[1] = 0
for i in range(2, int(k ** 0.5)):
    for p in range(i * 2, k, i):
        prime[p] = 0

ans = 0
for i in range(n):
    for j in range(i, n):
        if prime[j - i + 1] and prime[sum(data[i:j + 1])]:
            ans += 1
print(ans)
