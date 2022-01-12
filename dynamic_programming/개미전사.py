n = int(input())
data = list(map(int, input().split()))
check = [0] * 100
check[0] = data[0]
check[1] = max(data[0], data[1])
for i in range(2, n):
    check[i] = max(check[i - 1], check[i - 2] + data[i])
print(check[n - 1])