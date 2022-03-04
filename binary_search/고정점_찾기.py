import sys
def result(n, data):
    input = sys.stdin.readline
    # n = int(input())
    # data = list(map(int, input().rstrip().split()))
    left = 0
    right = n - 1
    asw = -1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] < mid:
            left = mid + 1
        elif data[mid] > mid:
            right = mid - 1
        else:
            asw = mid
            break
    print(asw)
result(5, [-15, -6, 1, 3, 7])
result(7, [-15, -4, 2, 8, 9, 13, 15])
result(7, [-15, -4, 3, 8, 9, 13, 15])