from collections import deque
n, k = map(int, input().split())
K = k
nums = list(map(int, list(input())))
d = deque()
for i in range(n):
    while k and d and d[-1] < nums[i]:
        d.pop()
        k -= 1
    d.append(nums[i])
print(''.join(map(str, list(d)[:n - K])))