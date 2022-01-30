import sys
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
count = [['' for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]
for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        if a[j - 1] == b[i - 1]:
            count[i][j] = count[i - 1][j - 1] + b[i - 1]
        else:
            if len(count[i - 1][j]) < len(count[i][j - 1]):
                count[i][j] = count[i][j - 1]
            else:
                count[i][j] = count[i - 1][j]
                count[i][j] = count[i - 1][j]
print(len(count[-1][-1]))
print(count[-1][-1])