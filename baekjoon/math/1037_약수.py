a = int(input())
data = list(map(int, input().split()))
data.sort()
if a % 2 == 1:
    print(data[a // 2] ** 2)
else:
    print(data[0] * data[-1])