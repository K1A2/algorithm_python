n = int(input())
all = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
all.sort()
def binary_search(target):
    isfind = False
    start, end = 0, n - 1
    while not isfind and start <= end:
        mid = (start + end) // 2
        if all[mid] < target:
            start = mid + 1
        elif all[mid] > target:
            end = mid - 1
        else:
            isfind = True
    return 'yes' if isfind else 'no'
for i in check:
    print(binary_search(i), end=' ')