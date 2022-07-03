import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input().rstrip())
line = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
ans = [0] * n
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    line[a].append(b)
    line[b].append(a)
def dfs(start, x, found, count):
    for nx in line[x]:
        if not visited[nx]:
            visited[nx] = 1
            found = dfs(start, nx, found, count + 1)
            if found:
                return found
            visited[nx] = 0
        else:
            if start == nx and count >= 3:
                return True
    return found
for i in range(1, n + 1):
    visited[i] = 1
    if dfs(i, i, False, 1):
        break
    visited[i] = 0

def dfs_find(x, count):
    ans[x - 1] = count
    for d in line[x]:
        if not visited[d]:
            visited[d] = 2
            dfs_find(d, count + 1)
            visited[d] = 0

for i in range(1, n + 1):
    if visited[i] == 1:
        for d in line[i]:
            if not visited[d]:
                visited[d] = 2
                dfs_find(d, 1)
print(*ans)