n = int(input())
x, y = 1, 1
for i in range(1, n):
    x, y = y, (x + y + 1) % 1000000007
print(y)
