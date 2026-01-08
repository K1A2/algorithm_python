import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
data = list(input().rstrip())
# dp = [0] * n
# dp[0] = 1
# for i in range(n):
#     if data[i] == '#': continue
#
#     if data[i - 1] != '#':
#         dp[i] += dp[i - 1]
#     if i - k >= 0 and data[i - k] != '#':
#         dp[i] += dp[i - k]
# print('YES' if dp[n - 1] > 0 else 'NO')

q = deque()
visited = [0] * n
visited[0] = 1
q.append(0)
while q:
    now = q.pop()
    if now + 1 < n and data[now + 1] != '#' and visited[now + 1] == 0:
        visited[now + 1] = 1
        q.append(now + 1)
    if now + k < n and data[now + k] != '#' and visited[now + k] == 0:
        visited[now +k] = 1
        q.append(now + k)
print('YES' if visited[n - 1] > 0 else 'NO')
