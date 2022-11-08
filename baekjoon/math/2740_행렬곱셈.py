import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
a = [list(map(int, input().rstrip().split())) for _ in range(n)]
m, k = map(int, input().rstrip().split())
b = [list(map(int, input().rstrip().split())) for _ in range(m)]

answer = []
for i in range(n):
    row = []
    for j in range(k):
        row.append(sum([a[i][l] * b[l][j] for l in range(m)]))
    answer.append(row)
for i in answer:
    print(*i)
