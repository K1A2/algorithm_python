import sys
n = int(sys.stdin.readline().rstrip())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
for i in range(n - 2, -1, -1):
    for j in range(len(data[i])):
        data[i][j] += max(data[i + 1][j], data[i + 1][j + 1])
print(data[0][0])