for _ in range(int(input())):
    n, m = map(int, input().split())
    n += 1
    m += 1
    data = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 1: data[i][j] = j
            if i == j: data[i][j] = 1
            elif j > i: data[i][j] = data[i][j - 1] + data[i - 1][j - 1]
    print(data[n - 1][m - 1])