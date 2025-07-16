n = int(input())
k = int(input())
low = 1
high = n ** 2
while low <= high:
    mid = (low + high) // 2
    count = 0
    for i in range(1, n + 1):
        count += min(mid // i, n)
    if count < k:
        low = mid + 1
    else:
        high = mid - 1
print(high + 1)
