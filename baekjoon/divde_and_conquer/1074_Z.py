n, r, c = map(int, input().split())
a = 4 ** (n - 1)
b = 2 ** (n - 1)
size = 2 ** n
result = 0
while a != 1:
    parts = ((b - 1, b - 1), (b - 1, b * 2 - 1), (b * 2 - 1, b - 1), (b * 2 - 1, b * 2 - 1))
    for i in range(len(parts)):
        if r <= parts[i][0] and c <= parts[i][1]:
            result += a * i
            if i == 1:
                c -= b
            elif i == 2:
                r -= b
            elif i == 3:
                r -= b
                c -= b
            b //= 2
            a //= 4
            break
parts = ((0,0), (0,1), (1,0), (1,1))
for i in range(len(parts)):
    if r <= parts[i][0] and c <= parts[i][1]:
        result += i
        break
print(result)