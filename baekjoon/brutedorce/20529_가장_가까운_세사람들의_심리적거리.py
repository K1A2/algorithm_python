from itertools import combinations
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    people = input().rstrip().split(' ')
    if n > 32:
        print(0)
        continue
    com = combinations(people, 3)
    ans = 100
    for i, j, k in com:
        res = 0
        res += sum([i[l] != j[l] for l in range(4)])
        res += sum([i[l] != k[l] for l in range(4)])
        res += sum([k[l] != j[l] for l in range(4)])
        ans = min(ans, res)
    print(ans)
