import sys
k, n = map(int, sys.stdin.readline().rstrip().split())
data = [int(sys.stdin.readline().rstrip()) for _ in range(k)]
start, end = 1, max(data)
result = 0
while start <= end:
    mid = (start + end) // 2
    total = sum([i // mid for i in data])
    if total < n:
        end = mid - 1
    elif total >= n:
        start = mid + 1
        if mid > result:
            result = mid
print(result)