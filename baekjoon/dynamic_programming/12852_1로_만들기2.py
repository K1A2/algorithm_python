x = int(input())
check = [[0, []] for _ in range(1000001)]
check[1][1] = [1]
for i in range(2, x + 1):
    check[i][0] = check[i - 1][0] + 1
    check[i][1] = check[i - 1][1] + [i]
    if i % 2 == 0 and check[i][0] > check[i // 2][0] + 1:
        check[i][0] = check[i // 2][0] + 1
        check[i][1] = check[i // 2][1] + [i]
    if i % 3 == 0 and check[i][0] > check[i // 3][0] + 1:
        check[i][0] = check[i // 3][0] + 1
        check[i][1] = check[i // 3][1] + [i]
print(check[x][0])
print(' '.join([str(check[x][1][i]) for i in range(check[x][0], -1, -1)]))