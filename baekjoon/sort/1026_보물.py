import sys
input = sys.stdin.readline
n = int(input().rstrip())
a = sorted(list(map(int, input().rstrip().split())))
b = sorted(list(map(int, input().rstrip().split())), reverse=True)
print(sum(a[i] * b[i] for i in range(n)))