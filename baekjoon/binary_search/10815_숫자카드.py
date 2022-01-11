import sys
n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()
m = int(sys.stdin.readline().rstrip())
def binary_search(target):
    result = 0
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] > target:
            end = mid - 1
        elif data[mid] < target:
            start = mid + 1
        else:
            result = 1
            break
    return result
for i in map(int, sys.stdin.readline().rstrip().split()):
    sys.stdout.write(str(binary_search(i)) + ' ')