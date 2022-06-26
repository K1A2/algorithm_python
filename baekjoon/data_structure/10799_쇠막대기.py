count = total = 0
prev_back = 0
for s in list(input()):
    if s == ')':
        count -= 1
        if prev_back:
            total += 1
        else:
            total += count
        prev_back = 1
    else:
        count += 1
        prev_back = 0
print(total)