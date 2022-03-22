import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
a1 = [list(map(int, input().rstrip().split())) for _ in range(n)]
a2 = [list(map(int, input().rstrip().split())) for _ in range(n)]
for x in range(n):
    for y in range(m):
        print(a1[x][y] + a2[x][y], end=' ')
    print()