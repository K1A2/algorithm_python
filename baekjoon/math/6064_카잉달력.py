import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    m, n, x, y = map(int, sys.stdin.readline().rstrip().split())
    solved = False
    while x <= m * n:
        if x % n == y % n:
            print(x)
            solved = True
            break
        x += m
    if not solved:
        print(-1)