import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    queue = deque()
    visited = [0] * 1000001
    visited[1] = 1
    queue.append((1 % n, '1'))
    while queue:
        mod, num = queue.popleft()
        if mod == 0:
            return num
        for i in range(2):
            n_mod = (mod * 10 + i) % n
            n_num = num + str(i)
            if not visited[n_mod]:
                visited[n_mod] = 1
                queue.append((n_mod, n_num))
    return 'BARK'

for _ in range(int(input())):
    print(bfs(int(input())))
