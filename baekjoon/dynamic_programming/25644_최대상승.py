n = int(input())
stock = list(map(int, input().split()))
m = v = 0
for i in range(n - 1, -1, -1):
    m = max(m, stock[i])
    v = max(v, m - stock[i])
print(v)
