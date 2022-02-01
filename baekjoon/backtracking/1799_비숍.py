import sys
n = int(sys.stdin.readline().rstrip())
availabe = [[], []]
availabe_len = [0, 0]
check_b = [0] * (2 * n - 1)
check_w = [0] * (2 * n - 1)
for i in range(n):
    d = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if d[j]:
            if (i + j) % 2 == 0:
                availabe[0].append((i, j))
                availabe_len[0] += 1
            else:
                availabe[1].append((i, j))
                availabe_len[1] += 1
asw = [0, 0]
def check(x, y):
    if check_w[x + y] or check_b[x - y + n - 1]:
        return False
    return True
def backtracking(count, start, idx):
    global asw
    if start == availabe_len[idx]:
        asw[idx] = max(asw[idx], count)
    else:
        for i in range(start, availabe_len[idx]):
            x, y = availabe[idx][i]
            if check(x, y):
                check_w[x + y] = check_b[x - y + n - 1] = 1
                backtracking(count + 1, i + 1, idx)
                check_w[x + y] = check_b[x - y + n - 1] = 0
backtracking(0, 0, 0)
backtracking(0, 0, 1)
print(sum(asw))