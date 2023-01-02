count = 1
while 1:
    a, b, c = map(int, input().split())
    if not a and not b and not c:
        break
    result = c // b * a
    result += c % b if c % b <= a else a
    print(f'Case {count}: {result}')
    count += 1