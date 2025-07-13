import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))
left = 0
right = n

next_one = [0] * (n + 1)
next_one[n] = n
for i in range(n-1, -1, -1):
    if data[i] == 1:
        next_one[i] = i
    else:
        next_one[i] = next_one[i+1]

def check(time):
    pos = n - 1
    for i in range(m):
        npos = pos - time
        if pos - time <= 0: return 1
        pos = next_one[npos]
        if pos >= n:
            return 0
    return 0

while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid
print(right)
