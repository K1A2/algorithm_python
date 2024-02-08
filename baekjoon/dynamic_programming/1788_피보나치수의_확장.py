n = int(input())
if n == 0:
    print(f'0\n0')
    exit()
x = 0
y = 1
for i in range(2, abs(n) + 1):
    x, y = y, (x + y) % 1000000000
print(f'{-1 if n % 2 == 0 and n < 0 else 1}\n{abs(y)}')
