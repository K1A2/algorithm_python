import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    data = [0] * 2
    for i in range(2):
        data[i] = list(map(int, input().rstrip().split()))
    for i in range(1, n):
        if i == 1:
            data[0][i] += data[1][i - 1]
            data[1][i] += data[0][i - 1]
            continue
        data[0][i] += max(data[1][i - 1], data[1][i - 2])
        data[1][i] += max(data[0][i - 1], data[0][i - 2])
    print(max(data[0][n - 1], data[1][n - 1]))