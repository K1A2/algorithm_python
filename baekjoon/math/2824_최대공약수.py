import sys
input = sys.stdin.readline
n = int(input().rstrip())
a = eval('*'.join(input().rstrip().split()))
m = int(input().rstrip())
b = eval('*'.join(input().rstrip().split()))

def gcd(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a
print(str(gcd(a, b))[-9:])