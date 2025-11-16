t = int(input())
wheel = [list(map(int, input())) for _ in range(t)]
gap = []
for i in range(t - 1):
    gap.append(wheel[i][2] != wheel[i + 1][-2])
# print(gap)

for _ in range(int(input())):
    idx, direction = map(int, input().split())
    if direction == 1:
        wheel[idx - 1] = [wheel[idx - 1][-1]] + wheel[idx - 1][:-1]
    else:
        wheel[idx - 1] = wheel[idx - 1][1:] + [wheel[idx - 1][0]]
    left = idx - 2
    right = idx
    move_left = 0
    if idx - 1 > 0:
        move_left = -direction if gap[left] else 0
    move_right = 0
    if idx - 1 < t - 1:
        move_right = -direction if gap[idx - 1] else 0
    while left >= 0 or right < t:
        if left >= 0:
            if move_left == 1:
                wheel[left] = [wheel[left][-1]] + wheel[left][:-1]
                gap[left] = wheel[left][2] != wheel[left + 1][-2]
                if left > 0:
                    move_left = -move_left if gap[left - 1] else 0
            elif move_left == -1:
                wheel[left] = wheel[left][1:] + [wheel[left][0]]
                gap[left] = wheel[left][2] != wheel[left + 1][-2]
                if left > 0:
                    move_left = -move_left if gap[left - 1] else 0
            else:
                gap[left] = wheel[left][2] != wheel[left + 1][-2]
                left = 0
            left -= 1
        if right < t:
            if move_right == 1:
                wheel[right] = [wheel[right][-1]] + wheel[right][:-1]
                gap[right - 1] = wheel[right - 1][2] != wheel[right][-2]
                if right < t - 1:
                    move_right = -move_right if gap[right] else 0
            elif move_right == -1:
                wheel[right] = wheel[right][1:] + [wheel[right][0]]
                gap[right - 1] = wheel[right - 1][2] != wheel[right][-2]
                if right < t - 1:
                    move_right = -move_right if gap[right] else 0
            else:
                gap[right - 1] = wheel[right - 1][2] != wheel[right][-2]
                right = t
            right += 1
    # print(wheel)
    # print(gap)
c = 0
for w in wheel:
    c += 1 if w[0] else 0
print(c)
