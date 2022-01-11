data = list(map(int, input().split()))
for i in range(1, len(data)):
    if abs(data[i] - data[i - 1]) != 1:
        print('mixed')
        exit()
if data[1] - data[0] == 1:
    print('ascending')
else:
    print('descending')