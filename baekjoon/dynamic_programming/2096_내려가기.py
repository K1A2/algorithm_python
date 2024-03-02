import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
dp_max = [i for i in data]
dp_min = [i for i in data]
for i in range(1, n):
    new_data = list(map(int, input().split()))
    dp_max_temp = [i for i in dp_max]
    dp_min_temp = [i for i in dp_min]
    dp_max = [0] * 3
    dp_min = [1e9] * 3
    for j in range(3):
        for dy in [-1, 0, 1]:
            ny = j + dy
            if 0 <= ny < 3:
                dp_max[j] = max(dp_max[j], dp_max_temp[ny] + new_data[j])
                dp_min[j] = min(dp_min[j], dp_min_temp[ny] + new_data[j])
print(f'{max(dp_max)} {min(dp_min)}')
