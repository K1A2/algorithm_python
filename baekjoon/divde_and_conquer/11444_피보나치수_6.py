n = int(input())
A = [[1, 1], [1, 0]]

def conquer(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            e = 0
            for k in range(2):
                e += a[i][k] * b[k][j]
            c[i][j] = e % 1000000007
    return c

def divide(a, k):
    if k == 1:
        return a
    b = divide(a, k // 2)
    if k % 2:
        return conquer(conquer(b, b), a)
    else:
        return conquer(b, b)
print(divide(A, n)[0][1])
