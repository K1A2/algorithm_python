import sys
input = sys.stdin.readline
n = int(input())
data = sorted(int(input()) for _ in range(n))
print(sum([abs(i - data[i - 1]) for i in range(1, n + 1)]))
