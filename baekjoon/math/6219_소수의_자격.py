prime = [1] * 4000001
for i in range(2, int(4000001 ** 0.5)):
    for p in range(i * 2, 4000001, i):
        prime[p] = 0
prime[0] = prime[1] = 0
a, b, c = map(int, input().split())
count = 0
for i in range(a, b + 1):
    if not prime[i]: continue
    if str(c) in str(i): count += 1
print(count)
