n = int(input())
for i in range(n):
    print((' *' * n) if i % 2 else ('* ' * (n - 1) + '*') , sep='')
