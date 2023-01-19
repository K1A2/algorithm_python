import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
lis = [data[0]]
idx = []

for i in data:
    if lis[-1] < i:
        idx.append(len(lis))
        lis.append(i)
    else:
        start = 0
        end = len(lis) - 1
        while start <= end:
            mid = (start + end) // 2
            if lis[mid] == i:
                start = mid
                break
            if lis[mid] < i:
                start = mid + 1
            else:
                end = mid - 1
        lis[start] = i
        idx.append(start)

log = deque()
target_idx = len(lis) - 1
i = n - 1
while target_idx >= 0 and i >= 0:
    if idx[i] == target_idx:
        log.appendleft(data[i])
        target_idx -= 1
    i -= 1
print(len(lis))
print(*log)
