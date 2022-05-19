n = 1000 - int(input())
res = 0
for i in [500, 100, 50, 10, 5, 1]:
    res += n // i
    n %= i
print(res)