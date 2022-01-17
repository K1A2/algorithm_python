a, b, c = map(int, input().split())
def fow(a, b):
    if b == 1:
        return a % c
    else:
        d = fow(a, b // 2)
        if b % 2 == 0:
            return d * d % c
        else:
            return d * d * a % c
print(fow(a, b))