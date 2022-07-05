import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
set_n = set(map(int, input().rstrip().split()))
set_m = set(map(int, input().rstrip().split()))
print(len(set_n - set_m) + len(set_m - set_n))
