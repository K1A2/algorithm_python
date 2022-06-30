data = list(map(int, input().split()))
def pro():
    for i in range(1, 5):
        if data[i - 1] > data[i]:
            data[i - 1], data[i] = data[i], data[i - 1]
            print(*data)
    if data != [1, 2, 3, 4, 5]:
        pro()
pro()