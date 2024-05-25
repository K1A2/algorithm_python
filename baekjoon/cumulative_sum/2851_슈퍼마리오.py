data = [int(input()) for _ in range(10)]
for i in range(1, 10):
    data[i] += data[i - 1]
ans = 10000
for i in range(10):
    if abs(100 - ans) > abs(data[i] - 100):
        ans = data[i]
    elif abs(100 - ans) == abs(data[i] - 100):
        ans = max(data[i], ans)
print(ans)
