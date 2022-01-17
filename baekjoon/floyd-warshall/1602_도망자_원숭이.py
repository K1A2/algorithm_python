import sys
inf = 10001
n, m, q = map(int, sys.stdin.readline().rstrip().split())
dog = list(map(int, sys.stdin.readline().rstrip().split()))
data = [[[inf, max(dog[i], dog[j])] for j in range(n)] for i in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    a -= 1
    b -= 1
    data[a][b][0] = data[b][a][0] = c

dog = sorted([(dog[i], i) for i in range(n)])
for d in dog:
    k = d[1]
    for a in range(n):
        for b in range(a + 1):
            if data[a][k] != inf and data[k][b] != inf:
                s = max(data[a][b][1], d[0])
                check1, check2 = data[a][b][0] + data[a][b][1], data[a][k][0] + data[k][b][0] + s
                if check1 > check2:
                    data[a][b][0] = data[b][a][0] = check2 - s
                    data[a][b][1] = data[b][a][1] = s

for _ in range(q):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    a -= 1
    b -= 1
    if data[a][b][0] == inf:
        sys.stdout.write('-1\n')
    else:
        sys.stdout.write(str(data[a][b][0] + data[a][b][1]) + '\n')