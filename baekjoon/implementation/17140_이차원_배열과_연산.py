from collections import defaultdict
r, c, k = map(int,input().split())
r -= 1
c -= 1
data = [list(map(int, input().split())) for _ in range(3)]

def sort_array(mode=0):
    count_data = []
    max_len = 0
    x_len, y_len = len(data), len(data[0])
    for i in range(y_len if mode else x_len):
        c_dict = defaultdict(int)
        for j in range(x_len if mode else y_len):
            now = data[j][i] if mode else data[i][j]
            if now == 0: continue
            c_dict[now] += 1
        items = list(c_dict.items())
        items.sort(key=lambda x: (x[1], x[0]))
        max_len = max(max_len, len(items) * 2)
        count_data.append(items)
    max_len = min(max_len, 100)

    new_data = []
    for count_item in count_data:
        new_section = []
        for j in range(min(len(count_item), 50)):
            new_section.extend(count_item[j])
        if len(new_section) < max_len:
            new_section.extend([0] * (max_len - len(new_section)))
        new_data.append(new_section)

    if mode:
        new_data = list(zip(*new_data))
    return new_data

count = 0
while 1:
    if 0 <= r < len(data) and 0 <= c < len(data[0]) and data[r][c] == k:
        break
    if count == 100:
        print(-1)
        exit()
    count += 1

    if len(data) >= len(data[0]): # r
        data = sort_array(mode=0)
    else: # c
        data = sort_array(mode=1)
print(count)
