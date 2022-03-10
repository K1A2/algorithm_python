import sys
import math
input = sys.stdin.readline
n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()
t = [data[i] - data[i - 1] for i in range(1, n)]
prev = t[0]
for i in range(1, n - 1):
    prev = math.gcd(prev, t[i])
ans = set()
for i in range(2, int(math.sqrt(prev) + 1)):
    if prev % i == 0:
       ans.add(i)
       ans.add(prev // i)
ans.add(prev)
print(*sorted(list(ans)))