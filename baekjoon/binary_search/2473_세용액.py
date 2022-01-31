import sys
n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()
res = ()
asw = int(1e11)
for start in range(n - 2):
    end = n - 1
    mid = start + 1
    while mid < end:
        total = data[start] + data[mid] + data[end]
        if abs(total) < asw:
            asw = abs(total)
            res = (data[start], data[mid], data[end])
        if total < 0:
            mid += 1
        elif total > 0:
            end -= 1
        else:
            print(' '.join([str(i) for i in res]))
            exit()
print(' '.join([str(i) for i in res]))