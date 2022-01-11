n, m = map(int, input().split())
data = list(map(int, input().split()))
start, end = 0, max(data)
while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in data:
        a = i - mid
        if a > 0:
            result += a
    if result == m:
        print(mid)
        exit()
    elif result > m:
        start = mid + 1
    else:
        end = mid - 1