import sys
n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))
start, end = 0, n - 1
min_gap = sys.maxsize
result = (str(data[start]), str(data[end]))
while start != end:
    now_gap = data[start] + data[end]
    if abs(now_gap) < min_gap:
        min_gap = abs(now_gap)
        result = (str(data[start]), str(data[end]))
    if now_gap > 0:
        end -= 1
    else:
        start += 1
print(' '.join(result))