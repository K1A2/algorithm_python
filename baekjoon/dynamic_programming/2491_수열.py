import sys
n = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))
dp_up, dp_down = [1] * n, [1] * n
for i in range(1, n):
    if data[i] <= data[i - 1]:
        dp_up[i] = max(dp_up[i], dp_up[i - 1] + 1)
    if data[i] >= data[i - 1]:
        dp_down[i] = max(dp_down[i], dp_down[i - 1] + 1)
print(max(max(dp_up), max(dp_down)))
