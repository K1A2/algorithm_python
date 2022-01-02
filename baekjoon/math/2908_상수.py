a, b = input().split()
a = a[2] + a[1] + a[0]
b = b[2] + b[1] + b[0]
print(max([int(a), int(b)]))