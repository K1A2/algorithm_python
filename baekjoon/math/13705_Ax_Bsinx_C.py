from decimal import *
import sys
input = sys.stdin.readline
getcontext().prec = 50
getcontext().rounding = ROUND_HALF_UP
pi = Decimal('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196')

a, b, c = map(Decimal, input().split())

# decimal sin 출처: https://docs.python.org/3/library/decimal.html#decimal-recipes
def sin(x):
    x = x % (2 * pi)
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

low, high = (c - b) / a, (c + b) / a
while high - low > Decimal(1e-25):
    mid = (low + high) / 2
    if a * mid + b * sin(mid) < c:
        low = mid
    else:
        high = mid
print(round(high, 6))
