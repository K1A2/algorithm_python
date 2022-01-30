import sys
n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()
start = 0
end = n - 1
asw = sys.maxsize
res = ()
while start < end:
    total = data[start] + data[end]
    if abs(total) < asw:
        asw = abs(total)
        res = (data[start], data[end])
    if total < 0:
        start += 1
    else:
        end -= 1
print(' '.join([str(i) for i in res]))