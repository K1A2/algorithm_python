n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if data[i][i] != 0:
        print(-1)
        exit()
    for j in range(n):
        if data[i][j] != data[j][i] or (i != j) and data[i][j] == 0:
            print(-1)
            exit()
        for k in range(n):
            if data[i][j] > data[i][k] + data[k][j]:
                print(-1)
                exit()

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        find = 0
        for k in range(n):
            if i == k or j == k: continue
            if data[i][j] == (data[i][k] + data[k][j]):
                find = 1
                break
        if not find:
            ans += data[i][j]
print(ans)
