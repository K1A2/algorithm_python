import sys
from collections import deque
a, b = map(int, sys.stdin.readline().rstrip().split())
d = deque()
def backtracking(n):
    if len(d) == b:
        print(*d)
        return
    for i in range(n, a + 1):
        d.append(i)
        backtracking(i)
        d.pop()
backtracking(1)