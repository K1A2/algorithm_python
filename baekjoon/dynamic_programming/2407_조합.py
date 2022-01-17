a, b = map(int, input().split())
data = [[-1] * (b + 1) for _ in range(a + 1)]
def com(a, b):
    if a == b or b == 0:
        data[a][b] = 1
        return 1
    else:
        if data[a][b] != -1:
            return data[a][b]
        else:
            data[a][b] = com(a - 1, b - 1) + com(a - 1, b)
        return data[a][b]
print(com(a, b))