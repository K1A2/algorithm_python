n = int(input())
x, y = 1, 1
for _ in range(n - 1):
    x, y = y, (x + y) % 10
print(y)
