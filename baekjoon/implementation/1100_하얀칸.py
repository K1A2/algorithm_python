data = [input() for _ in range(8)]
count = 0
for x in range(8):
    for y in range(8):
        if abs(x - y) % 2 == 0 and data[x][y] == 'F':
            count += 1
print(count)