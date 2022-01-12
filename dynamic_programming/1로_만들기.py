x = int(input())
check = [0] * 30001
for i in range(2, x + 1):
    check[i] = check[i - 1] + 1
    if i % 2 == 0:
        check[i] = min(check[i], check[i // 2] + 1)
    if i % 3 == 0:
        check[i] = min(check[i], check[i // 3] + 1)
    if i % 5 == 0:
        check[i] = min(check[i], check[i // 5] + 1)
print(check[x])