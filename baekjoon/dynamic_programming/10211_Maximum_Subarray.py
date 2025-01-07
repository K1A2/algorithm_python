for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    data = [0] + data
    small = [0] * (n + 1)
    small[1] = min(small[0], data[0])
    res = -(10 ** 7)
    for i in range(1, n + 1):
        data[i] += data[i - 1]
        small[i] = min(small[i - 1], data[i])
        res = max(data[i] - small[i - 1], res)
    print(res)
