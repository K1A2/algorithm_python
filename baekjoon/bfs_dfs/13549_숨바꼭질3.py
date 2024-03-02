import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

max_len = 100000 + 1

visited = [-1] * max_len

d = deque()
d.append((a, 0))
visited[a] = 1

while d:
    pos, sec = d.popleft()
    if pos == b:
        print(sec)
        break
    for np in [pos * 2, pos + 1, pos - 1]:
        if 0 <= np < max_len:
            ns = sec + (0 if pos * 2 == np else 1)
            if visited[np] == -1 or ns < visited[np]:
                visited[np] = min(visited[np], ns) if visited[np] != -1 else ns
                if pos * 2 == np:
                    d.appendleft((np, ns))
                else:
                    d.append((np, ns))
