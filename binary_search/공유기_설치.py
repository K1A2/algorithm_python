import sys
def result(n, c, data):
    data.sort()
    start = 1
    end = data[-1] - data[0]
    res = 0
    while start <= end:
        mid = (start + end) // 2
        prev_idx = 0
        count = 1
        for i in range(1, n):
            if data[i] - data[prev_idx] >= mid:
                prev_idx = i
                count += 1
        if count < c:
            end = mid - 1
        else:
            res = max(res, mid)
            start = mid + 1
    print(res)
result(5, 3, [1, 2, 8, 4, 9])