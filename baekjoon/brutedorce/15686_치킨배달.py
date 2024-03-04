import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
chicken = []
house = []
for i in range(n):
    row = list(map(int, input().split()))
    for j, r in enumerate(row):
        if r == 2:
            chicken.append((i, j))
        if r == 1:
            house.append((i, j))

ans = 1e10
for com in combinations(range(len(chicken)), m):
    s = []
    for c in com:
        s.append([abs(h[0] - chicken[c][0]) + abs(h[1] - chicken[c][1]) for h in house])
    ans = min(ans, sum([min([s[j][i] for j in range(m)]) for i in range(len(house))]))
print(ans)
