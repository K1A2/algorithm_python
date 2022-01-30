import sys
n, s = map(int, sys.stdin.readline().rstrip().split())
n += 1
data = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(1, n):
    data[i] = data[i - 1] + data[i]
start = 0
end = 1
result = sys.maxsize
while start != n:
    all = data[end] - data[start]
    if all <= s:
        if all == s:
            result = min(result, end - start)
        if end != n - 1:
            end += 1
        else:
            start += 1
    else:
        result = min(result, end - start)
        start += 1
if result == sys.maxsize:
    result = 0
print(result)