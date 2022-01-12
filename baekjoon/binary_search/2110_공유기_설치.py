import sys
n, c = map(int, sys.stdin.readline().rstrip().split())
data = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
data.sort()
start, end = 1, data[-1] - data[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    count = 1
    prev_idx = 0
    for i in range(1, n):
        if data[i] - data[prev_idx] >= mid:
            count += 1
            prev_idx = i
    if count < c:
        end = mid - 1
    else:
        result = max([result, mid])
        start = mid + 1
print(result)