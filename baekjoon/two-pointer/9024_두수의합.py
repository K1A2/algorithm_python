import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()

    delta = 2e9
    count = 0
    for i in range(n):
        left = i + 1
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            s = data[i] + data[mid]
            if s > m:
                right = mid - 1
            else:
                left = mid + 1
            if abs(m - s) < delta:
                count = 1
                delta = abs(m - s)
            elif abs(m - s) == delta:
                count += 1
    print(count)
