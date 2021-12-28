data = list(map(int, input()))

def change(target):
    count = 0
    prev = 2
    for i in data:
        if i != target and prev != i:
            count += 1
        prev = i
    return count

print(min(change(0), change(1)))