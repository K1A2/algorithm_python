prime = [1] * 1000001
for i in range(2, int(1000001 ** 0.5)):
    for p in range(i * 2, 1000001, i):
        prime[p] = 0
prime[0] = prime[1] = 0

n = int(input())
data = list(set(map(int, input().split())))
ans = 1
for i in data:
    if prime[i]:
        ans *= i
print(-1 if ans == 1 else ans)
