n = int(input())
k = 104729
prime = [1] * (k + 1)
prime[0] = prime[1] = 0
for i in range(2, int((k + 1) ** (1 / 2)) + 1):
    for j in range(i * 2, k + 1, i):
        prime[j] = 0
idx = 1
i = 0
while i < n:
    if prime[idx]:
        i += 1
    idx += 1
print(idx - 1)
