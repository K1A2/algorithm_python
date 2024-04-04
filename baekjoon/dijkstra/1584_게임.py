import sys
import heapq
input = sys.stdin.readline

def get_data(n):
    l = []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        if a > c:
            a, c = c, a
        if b > d:
            b, d = d, b
        l.append((a, b, c, d))
    return l

n = int(input())
danger = get_data(n)
m = int(input())
forbidden = get_data(m)
distance = [[sys.maxsize] * 501 for _ in range(501)]

def dijkstra():
    dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))
    q = [(0, 0, 0)]
    distance[0][0] = 0
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 501 and 0 <= ny < 501:
                c = 0
                for fx1, fy1, fx2, fy2 in forbidden:
                    if fx1 <= nx <= fx2 and fy1 <= ny <= fy2:
                        c = 1
                        break
                if c: continue
                n_dist = dist
                for fx1, fy1, fx2, fy2 in danger:
                    if fx1 <= nx <= fx2 and fy1 <= ny <= fy2:
                        n_dist += 1
                        break
                if n_dist < distance[nx][ny]:
                    distance[nx][ny] = n_dist
                    heapq.heappush(q, (n_dist, nx, ny))

dijkstra()
print(distance[-1][-1] if distance[-1][-1] != sys.maxsize else -1)
