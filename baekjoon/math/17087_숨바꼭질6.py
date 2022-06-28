n, s = map(int, input().split())
data = list(set([abs(i - s) for i in map(int, input().split())]))
def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a
if len(data) == 1:
    print(data[0])
else:
    a = gcd(data[0], data[1])
    for i in range(2, len(data)):
        a = gcd(a, data[i])
    print(a)