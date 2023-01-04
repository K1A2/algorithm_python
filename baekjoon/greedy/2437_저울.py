n = int(input())
data = sorted(map(int, input().split()))
target = 1
for i in range(n):
    if target < data[i]:
        break
    target += data[i]
print(target)
