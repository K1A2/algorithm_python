from collections import deque
from sys import stdin
h, w = map(int, stdin.readline().rstrip().split())
objects = [0,0] # R B
map_data = []
for i in range(h):
    a = list(stdin.readline().rstrip())
    for j in range(w):
        if a[j] == 'R':
            objects[0] = (i, j)
            a[j] = '.'
        elif a[j] == 'B':
            objects[1] = (i, j)
            a[j] = '.'
    map_data.append(a)
dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
que = deque()
que.append((objects[0], objects[1], [','.join(map(str,objects[0])),','.join(map(str,objects[1]))], 0))
while que:
    r, b, visited, count = que.popleft()
    visited_0 = [i for i in visited[0].split()]
    visited_1 = [i for i in visited[1].split()]
    if count >= 10:
        continue
    for idx in range(len(dxy)):
        d = dxy[idx]
        r_new, b_new = None, None
        hole = 0
        nrx, nry, nbx, nby = r[0], r[1], b[0], b[1]
        while True:
            nrx += d[0]
            nry += d[1]
            if map_data[nrx][nry] == '#':
                nrx -= d[0]
                nry -= d[1]
                if nrx == r[0] and nry == r[1]:
                    r_new = (nrx, nry)
                    break
                r_new = (nrx, nry)
                break
            elif map_data[nrx][nry] == 'O':
                hole = 1
                break
        while True:
            nbx += d[0]
            nby += d[1]
            if map_data[nbx][nby] == '#':
                nbx, nby = nbx - d[0], nby - d[1]
                if nbx == b[0] and nby == b[1]:
                    if nrx == r[0] and nry == r[1]:
                        break
                    b_new = (nbx, nby)
                    break
                if str(nbx) + ',' + str(nby) in visited_1 and str(nrx) + ',' + str(nry) in visited_0:
                    break
                b_new = (nbx, nby)
                break
            elif map_data[nbx][nby] == 'O':
                hole = 2
                break
        if r_new and b_new:
            if r_new == b_new:
                if idx == 0:
                    if r[0] < b[0]:
                        b_new = (b_new[0] + 1, b_new[1])
                    else:
                        r_new = (r_new[0] + 1, r_new[1])
                elif idx == 1:
                    if r[0] < b[0]:
                        r_new = (r_new[0] - 1, r_new[1])
                    else:
                        b_new = (b_new[0] - 1, b_new[1])
                elif idx == 2:
                    if r[1] < b[1]:
                        b_new = (b_new[0], b_new[1] + 1)
                    else:
                        r_new = (r_new[0], r_new[1] + 1)
                elif idx == 3:
                    if r[1] < b[1]:
                        r_new = (r_new[0], r_new[1] - 1)
                    else:
                        b_new = (b_new[0], b_new[1] - 1)
            visited_0.append(str(r_new[0]) + ',' + str(r_new[1]))
            visited_1.append(str(b_new[0]) + ',' + str(b_new[1]))
            que.append((r_new, b_new, [' '.join([str(v[0]) + ',' + str(v[1]) for v in i]) for i in [set(visited_0), set(visited_1)]], count + 1))
        elif hole == 1:
            print(count + 1)
            exit()
print(-1)