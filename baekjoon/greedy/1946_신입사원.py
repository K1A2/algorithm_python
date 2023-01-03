import sys
input = sys.stdin.readline
for _ in range(int(input())):
    count = 1
    data = [list(map(int, input().split())) for _ in range(int(input()))]
    data = sorted(data, key=lambda x: x[0])
    least = data[0][1]
    for i in range(1, len(data)):
        if data[i][1] < least:
            count += 1
            least = data[i][1]
    print(count)
