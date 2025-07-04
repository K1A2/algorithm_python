import sys
input = sys.stdin.readline
n = int(input())
crane = sorted(list(map(int, input().split())))
m = int(input())
cargo = sorted(list(map(int, input().split())))

if crane[-1] < cargo[-1]:
    print(-1)
    exit()

idx = [0] * n
moved = [1] * m
check = m - 1
for i in range(n - 1, -1, -1):
    while 1:
        if check == -1:
            idx[i] = check
            break
        if cargo[check] <= crane[i]:
            idx[i] = check
            break
        check -= 1

res = 0
while sum(moved) != 0:
    for i in range(n):
        if idx[i] == -1:
            continue
        while idx[i] >= 0:
            if moved[idx[i]] == 1:
                moved[idx[i]] = 0
                break
            idx[i] -= 1
    res += 1
print(res)
