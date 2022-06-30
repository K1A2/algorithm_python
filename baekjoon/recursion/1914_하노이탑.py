n = int(input())
l = []
def hanoi(n, f, t, m):
    if n == 1:
        l.append((f, t))
        return
    hanoi(n - 1, f, m, t)
    l.append((f, t))
    hanoi(n - 1, m, t, f)
if n <= 20:
    hanoi(n, 1, 3, 2)
    print(len(l))
    for i in l: print(*i)
else:
    print(2 ** n - 1)