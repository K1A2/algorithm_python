n = int(input())
data = input().split()

available = [1] * 10
min_num = '9999999999'
max_num = '0000000000'

def backtracking(number, pos):
    global min_num, max_num

    if pos == n:
        if int(min_num) > int(number):
            min_num = number
        if int(max_num) < int(number):
            max_num = number
        return

    for i in range(10):
        if not available[i]: continue
        if data[pos] == '<':
            if int(number[-1]) >= i: continue
        elif data[pos] == '>':
            if int(number[-1]) <= i: continue
        available[i] = 0
        backtracking(number + str(i), pos + 1)
        available[i] = 1

for i in range(10):
    available[i] = 0
    backtracking(str(i), 0)
    available[i] = 1

print(max_num)
print(min_num)
