n = int(input())
if n == 0:
    print(0)
    exit()
scores = sorted([int(input()) for _ in range(n)])
cut = round(n * 0.15 + 1e-12)
print(round(sum([scores[i] for i in range(cut, n - cut)]) / (n - cut * 2) + 1e-12))
