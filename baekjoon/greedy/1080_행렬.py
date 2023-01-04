import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [input().rstrip() for _ in range(n)]
b = [input().rstrip() for _ in range(n)]
if (n < 3 or m < 3) and a != b:
    print(-1)
    exit()
data = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(int(a[i][j] != b[i][j]))
    data.append(row)
count = 0
for i in range(n - 2):
    for j in range(m - 2):
        if data[i][j]:
            count += 1
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    data[k][l] = 1 - data[k][l]
print(-1 if sum([sum(d) for d in data]) else count)
