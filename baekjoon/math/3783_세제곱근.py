import sys
from decimal import *
input = sys.stdin.readline
getcontext().prec = 500
for _ in range(int(input())):
    n = Decimal(input().rstrip())
    ans = n ** (Decimal('1') / Decimal('3'))
    print(str(round(ans, 102))[:-92])
