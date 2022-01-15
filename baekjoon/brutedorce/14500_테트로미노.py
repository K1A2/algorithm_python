import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
shape = (((0, 0), (1, 0), (2, 0), (3, 0)), ((0, 0), (0, 1), (0, 2), (0, 3)),
         ((0, 0), (0, 1), (1, 0), (1, 1)), ((0, 0), (0, -1), (1, 0), (1, -1)),
         ((0, 0), (1, 0), (2, 0), (2, 1)), ((0, 0), (0, 1), (0, 2), (1, 2)),
         ((0, 0), (1, 0), (2, 0), (2, -1)), ((0, 0), (0, 1), (0, 2), (-1, 2)),
         ((0, 0), (1, 0), (1, 1), (2, 1)), ((0, 0), (1, 0), (1, -1), (2, -1)),
         ((0, 0), (0, 1), (1, 1), (1, 2)), ((0, 0), (0, 1), (-1, 1), (-1, 2)),
         ((0, 0), (0, 1), (0, 2), (1, 1)), ((0, 0), (0, 1), (0, 2), (-1, 1)),
         ((0, 0), (1, 0), (2, 0), (1, 1)), ((0, 0), (1, 0), (2, 0), (1, -1)))
result = 0
for x in range(n):
    for y in range(m):
        for i in shape:
            score1 = score2 = 0
            for j in i:
                if 0 <= x + j[0] < n and 0 <= y + j[1] < m:
                    score1 += data[x + j[0]][y + j[1]]
                if 0 <= x + -j[0] < n and 0 <= y + -j[1] < m:
                    score2 += data[x + -j[0]][y + -j[1]]
            result = max(result, score1, score2)
print(result)