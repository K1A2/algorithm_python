import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(i, visited, data):
    if visited[i]:
        return 1
    visited[i] = 1
    return dfs(data[i], visited, data)

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    data = [0] + list(map(int, input().rstrip().split()))
    visited = [0] * (n + 1)
    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            count += dfs(i, visited, data)
    print(count)
