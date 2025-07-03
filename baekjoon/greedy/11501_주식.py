import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().rstrip().split()))
    sell = data[-1]
    res = 0
    for i in range(n - 2, -1, -1):
        if data[i] >= sell:
            sell = data[i]
        else:
            res += sell - data[i]
    print(res)
