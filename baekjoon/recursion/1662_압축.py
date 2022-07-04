a = input()
n = len(a)
def find(start, count):
    i = start
    while i < n:
        if a[i] == '(':
            c, idx = find(i + 1, 0)
            count += int(a[i - 1]) * c - 1
            i = idx
        elif a[i] == ')':
            return count, i
        else:
            count += 1
        i += 1
    return count, i
print(find(0, 0)[0])