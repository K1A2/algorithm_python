import sys
input = sys.stdin.readline
n = int(input().rstrip())
s = list(map(int, input().rstrip().split()))
target = int(input().rstrip())
s.sort()
start = end = -1
if target < s[0]:
    start = 1
    end = s[0] - 1
else:
    for i in range(n - 1):
        if s[i] < target < s[i + 1]:
            start = s[i] + 1
            end = s[i + 1] - 1
            break
if end == -1:
    print(0)
else:
    count = 0
    for i in range(start, target + 1):
        for j in range(target, end + 1):
            if i == j: continue
            count += 1
    print(count)