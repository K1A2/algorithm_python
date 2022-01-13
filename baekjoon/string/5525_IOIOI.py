import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
data = sys.stdin.readline().rstrip()
count = 0
check = 0
start = 0
while start < m - 2:
    if data[start] == 'I' and data[start + 1] == 'O' and data[start + 2] == 'I':
        check += 1
        if check == n:
            count += 1
            check -= 1
        start += 2
    else:
        check = 0
        start += 1
print(count)