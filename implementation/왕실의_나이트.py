k = input()
x, y = ord(k[0]) - ord('a'), int(k[1]) - 1

check = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
count = 0
for i in check:
    if 0 <= x + i[0] <= 7 and 0 <= y + i[1] <= 7:
        count += 1
print(count)