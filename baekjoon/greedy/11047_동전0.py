n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
count = 0
for i in range(len(coins) - 1, -1, -1):
    if k == 0:
        break
    if k < coins[i]:
        continue
    count += k // coins[i]
    k %= coins[i]
print(count)