import sys
input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    data = [input().rstrip() for _ in range(n)]
    data.sort()

    found = 0
    for i in range(n - 1):
        if data[i + 1].startswith(data[i]):
            print('NO')
            found = 1
            break
    if not found:
        print('YES')