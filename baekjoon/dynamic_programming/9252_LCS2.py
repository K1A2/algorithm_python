import sys
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())
count = [[''] * (len(b) + 1) for _ in range(len(a) + 1)]
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            count[i][j] = count[i - 1][j - 1] + a[i - 1]
        else:
            if len(count[i - 1][j]) < len(count[i][j - 1]):
                count[i][j] = count[i][j - 1]
            else:
                count[i][j] = count[i - 1][j]
print(len(count[-1][-1]))
print(count[-1][-1])