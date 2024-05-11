n = int(input())
k = 7500000
prime = [1] * (k + 1)
prime[0] = prime[1] = 0
for i in range(2, int((k + 1) ** 0.5)):
    for p in range(i * 2, k + 1, i):
        prime[p] = 0
count = 1
num = 2
while count < n:
    num += 1
    if prime[num]:
        count += 1
print(num)
