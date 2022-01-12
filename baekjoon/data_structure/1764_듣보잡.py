import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
data = set([sys.stdin.readline().rstrip() for _ in range(n)])
result = []
count = 0
for _ in range(m):
    a = sys.stdin.readline().rstrip()
    if a in data:
        count += 1
        result.append(a)
        continue
result.sort()
print(count)
sys.stdout.write('\n'.join(result))