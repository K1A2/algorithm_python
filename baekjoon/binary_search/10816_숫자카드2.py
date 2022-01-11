# 딕셔너리가 더욱 빠름. https://www.acmicpc.net/board/view/77672
import sys
n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()
# data_dict = dict()
# for i in data:
#     if i in data_dict:
#         data_dict[i] += 1
#     else:
#         data_dict[i] = 1
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
            result += 1
            now = mid - 1
            while 0 <= now and data[now] == target:
                now -= 1
            result += mid - now - 1
            now = mid + 1
            while now < n and data[now] == target:
                now += 1
            result += now - mid - 1
            break
    return result
for i in map(int, sys.stdin.readline().rstrip().split()):
    sys.stdout.write(str(binary_search(i)) + ' ')