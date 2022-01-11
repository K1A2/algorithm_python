n, k = map(int, input().split())
people = [i for i in range(1, n + 1)]
result = []
prev = 0
while len(people) > 0:
    prev += k - 1
    while prev >= len(people):
        prev -= len(people)
    result.append(str(people.pop(prev)))
print('<', end='')
print(', '.join(result), end='')
print('>', end='')