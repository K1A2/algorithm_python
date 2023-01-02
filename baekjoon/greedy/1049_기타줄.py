import sys
input = sys.stdin.readline
n, m = map(int, input().split())
six_lines, one_lines = [], []
for _ in range(m):
    a, b = map(int, input().split())
    six_lines.append(a)
    one_lines.append(b)

cost = 0
six_min, one_min = min(six_lines), min(one_lines)
if six_min < one_min * 6:
    cost += six_min * (n // 6)
else:
    cost += one_min * 6 * (n // 6)
s = n % 6
if six_min < one_min * s:
    cost += six_min
else:
    cost += one_min * s
print(cost)
