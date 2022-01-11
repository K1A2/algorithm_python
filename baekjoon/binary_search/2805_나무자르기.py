n, m = map(int, input().split())
data = list(map(int, input().split()))
start, end = 0, 2000000000
result = 0
while start <= end:
    mid = (start + end) // 2
    cut = sum(i - mid if i > mid else 0 for i in data)
    if cut > m:
        if mid > result:
            result = mid
        start = mid + 1
    elif cut < m:
        end = mid - 1
    else:
        result = mid
        break
print(result)