a, b = list(map(int, input().split()))
check = [False, False] + [True] * (b - 1)
s = ''
if a < 2:
    a = 2
for i in range(2, b + 1):
    if check[i]:
        if a <= i:
            s += str(i) + "\n"
        for j in range(2 * i, b + 1, i):
            check[j] = False
print(s, end="")