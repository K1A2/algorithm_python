import sys
input = sys.stdin.readline
while 1:
    n = int(input())
    if n == 0:
        break
    data = [int(input()) for _ in range(n)]
    for i in range(1, n):
        data[i] = max(data[i], data[i - 1] + data[i])
    print(max(data))
