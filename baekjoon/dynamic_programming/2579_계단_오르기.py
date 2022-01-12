import sys
n = int(sys.stdin.readline().rstrip())
data = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
if n < 3:
    print(sum(data))
    exit()
check = [0 for _ in range(n)]
check[-1] = data[-1]
check[-2] = data[-1] + data[-2]
check[-3] = data[-1] + data[-3]
for i in range(n - 4, -1, -1):
    check[i] = max(data[i] + check[i + 2], check[i + 3] + data[i + 1] + data[i])
print(max(check[0], check[1]))