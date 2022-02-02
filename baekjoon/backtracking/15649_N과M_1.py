import sys
from collections import deque
a, b = map(int, sys.stdin.readline().rstrip().split())
d = deque()
def backtracking():
    if len(d) == b:
        print(*d)
    for i in range(1, a + 1):
        if i in d:
            continue
        d.append(i)
        backtracking()
        d.pop()
backtracking()