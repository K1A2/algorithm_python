n = int(input())
data = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
data.sort()
def binary_search(target):
    start, end = 0, n - 1
    find = False
    while not find and start <= end:
        mid = (start + end) // 2
        if data[mid] > target:
            end = mid - 1
        elif data[mid] < target:
            start = mid + 1
        else:
            find = True
    return 1 if find else 0
for i in check:
    print(binary_search(i))