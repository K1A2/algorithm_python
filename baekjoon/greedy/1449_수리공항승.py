n, l = map(int, input().split())
data = sorted(map(int, input().split()))
start = end = idx = count = result = 0
while idx < n:
    if not count:
        start = end = data[idx]
        count = 1
    else:
        end = data[idx]
        count += 1
    if end - start + 1 > l:
        result += 1
        count = 1
        start = end
    idx += 1
print(result + 1)
