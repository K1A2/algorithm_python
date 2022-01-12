import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
save = dict()
for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    save[a] = b
for _ in range(m):
    print(save[sys.stdin.readline().rstrip()])