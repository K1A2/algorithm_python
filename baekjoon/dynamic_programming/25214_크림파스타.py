n = int(input())
data = list(map(int, input().split()))
result = [0]
mi = data[0]
for i in range(1, n):
    if mi > data[i]:
        mi = data[i]
    result.append(max(data[i] - mi, result[-1]))
print(' '.join(map(str, result)))
