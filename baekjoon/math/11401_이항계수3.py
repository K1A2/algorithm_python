a, b = map(int, input().split())
p = 1000000007
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i % p
    return res
def square(c, n):
    if n == 1:
        return c
    if n == 0:
        return 1
    tmp = square(c, n // 2)
    if n % 2:
        return tmp * tmp * c % p
    else:
        return tmp * tmp % p
print(factorial(a) * square(factorial(b) * factorial(a - b) % p, p - 2) % p)