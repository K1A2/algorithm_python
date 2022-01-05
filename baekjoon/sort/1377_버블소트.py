from sys import stdin
n = int(stdin.readline())
l = []
for i in range(n):
    num = int(stdin.readline())
    l.append([num, i])
l.sort()
m = 0
for i in range(n):
    if m < l[i][1] - i:
        m = l[i][1] - i
print(m + 1)