a = input()
b = input()

def gcd(l1, l2):
    if l2 > l1:
        l1, l2 = l2, l1
    while l2 != 0:
        l1, l2 = l2, l1 % l2
    return l1
l = len(a) * len(b) // gcd(len(a), len(b))
if a * (l // len(a)) == b * (l // len(b)):
    print(1)
else:
    print(0)