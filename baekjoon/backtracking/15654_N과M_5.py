import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
data = sorted(list(map(int, input().rstrip().split())))
use = set()
def backtracking(depth, now):
    if depth == m:
        print(*now)
    for i in range(n):
        if i in use:
            continue
        now.append(data[i])
        use.add(i)
        backtracking(depth + 1, now)
        now.pop()
        use.remove(i)
backtracking(0, [])