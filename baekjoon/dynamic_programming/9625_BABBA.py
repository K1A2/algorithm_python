n = int(input())
a, b = [0] * 46, [0] * 46
a[0] = b[1] = 1
for i in range(2, n + 1):
    a[i] = a[i - 1] + a[i - 2]
    b[i] = b[i - 1] + b[i - 2]
print(a[n], b[n])