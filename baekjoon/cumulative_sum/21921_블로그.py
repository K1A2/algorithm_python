import sys
input = lambda : sys.stdin.readline()
n, m = map(int, input().split())
data = list(map(int, input().split()))
for i in range(1, n):
    data[i] += data[i - 1]
start = 1
end = start + m - 1
max_value = data[end - 1]
count = 1
while end < n:
     v = data[end] - data[start - 1]
     if v > max_value:
         max_value = v
         count = 1
     elif v == max_value:
         count += 1
     end += 1
     start += 1
if max_value == 0:
    print('SAD')
else:
    print(max_value)
    print(count)
