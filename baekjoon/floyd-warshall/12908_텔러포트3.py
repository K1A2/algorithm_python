import sys
input = sys.stdin.readline
sx, sy = map(int, input().split())
hx, hy = map(int, input().split())
tp = [list(map(int, input().split())) for _ in range(3)]
graph = [[sys.maxsize] * 8 for _ in range(8)]
for i in range(8):
    graph[i][i] = 0
pos = [(sx, sy)]
for i in tp:
    pos.append((i[0], i[1]))
    pos.append((i[2], i[3]))
pos.append((hx, hy))
for i in range(8):
    for j in range(i + 1, 8):
        graph[i][j] = abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1])
        graph[j][i] = abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1])
        for t in tp:
            if t[0] == pos[i][0] and t[1] == pos[i][1] and t[2] == pos[j][0] and t[3] == pos[j][1]:
                graph[i][j] = 10
                graph[j][i] = 10
                break
for k in range(8):
    for i in range(8):
        for j in range(8):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
print(graph[-1][0])
