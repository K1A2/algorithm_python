import sys
from decimal import *
getcontext().prec = 100
input = sys.stdin.readline
left = Decimal('-1000001')
right = Decimal('1000001')
func = lambda x: (a * x ** 3) + (b * x ** 2) + (c * x) + d
p = 20

def get_point(a: Decimal, b: Decimal, c: Decimal):
    d = b ** 2 - 4 * a * c
    if d > 0:
        root1 = (-b - d.sqrt()) / (2 * a)
        root2 = (-b + d.sqrt()) / (2 * a)
        return (root1, root2)
    elif d == 0:
        multiple = (-b + d.sqrt()) / (2 * a)
        return (multiple,)
    else:
        return ()

def bisection(low, high):
    while high - low > Decimal(1e-25):
        mid = (low + high) / 2
        if func(mid) * func(low) > 0:
            low = mid
        else:
            high = mid
    return low

for _ in range(int(input())):
    a, b, c, d = map(Decimal, input().split())
    points = get_point(3 * a, 2 * b, c)
    ans = []
    if len(points) == 0:
        ans.append(bisection(left, right))
    elif len(points) == 1:
        if round(func(left) * func(points[0]), p) <= 0:
            ans.append(bisection(left, points[0]))
        else:
            ans.append(bisection(points[0], right))
    else:
        points = [min(points), max(points)]
        if round(func(points[0]) * func(points[1]), p) <= 0:
            if round(func(points[0]), p) == 0:
                ans = [points[0], bisection(points[1], right)]
            elif round(func(points[1]), p) == 0:
                ans = [bisection(left, points[0]), points[1]]
            else:
                ans = [bisection(left, points[0]), bisection(points[0], points[1]), bisection(points[1], right)]
        else:
            if round(func(left) * func(points[0]), p) <= 0:
                ans = [bisection(left, points[0])]
            else:
                ans = [bisection(points[1], right)]
    ans.sort()
    print(' '.join(map(lambda x: f'{x:.10f}', ans)))
