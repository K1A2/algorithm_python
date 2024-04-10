import sys
input = sys.stdin.readline
n = int(input())
alphabet = ord('z') - ord('A') + 1
graph = [[sys.maxsize] * alphabet for _ in range(alphabet)]
for _ in range(n):
    a, b = map(lambda x: ord(x) - ord('A'), input().rstrip().split(' => '))
    graph[a][b] = 1
for k in range(alphabet):
    graph[k][k] = 1
    for i in range(alphabet):
        for j in range(alphabet):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
res = []
for i in range(alphabet):
    for j in range(alphabet):
        if i == j:
            continue
        if graph[i][j] != sys.maxsize:
            res.append(f'{chr(i + ord("A"))} => {chr(j + ord("A"))}')
print(len(res))
print('\n'.join(res))
