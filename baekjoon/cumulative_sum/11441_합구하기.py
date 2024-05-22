import sys
input = lambda : sys.stdin.readline()
n = int(input())
data = list(map(int, input().split()))
for i in range(1, n):
    data[i] += data[i - 1]
for _ in range(int(input())):
    a, b = map(lambda x: int(x) - 1, input().split())
    ans = data[b]
    if a - 1 >= 0:
        ans -= data[a - 1]
    print(ans)
