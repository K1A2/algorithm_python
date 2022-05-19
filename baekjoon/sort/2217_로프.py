import sys
input = sys.stdin.readline
n = int(input().rstrip())
nums = sorted([int(input().rstrip()) for _ in range(n)], reverse=True)
res = 0
for i in range(n):
    once = nums[i] * (i + 1)
    res = max(res, once)
print(res)