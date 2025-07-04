import sys
input = sys.stdin.readline
n = int(input())
switch = list(map(int, input().split()))
for _ in range(int(input())):
    s, a = map(int, input().split())
    a -= 1
    if s == 1:
        for i in range(a, n, a + 1):
            switch[i] = abs(switch[i] - 1)
    else:
        r = l = a
        while l >= 0 and r < n:
            if switch[l] != switch[r]:
                break
            l -= 1
            r += 1
        for i in range(l + 1, r):
            switch[i] = abs(switch[i] - 1)
for i in range(0, n, 20):
    print(*switch[i:i + 20])
