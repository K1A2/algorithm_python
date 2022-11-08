import re
data = re.sub('[^UCP]', '', input())
check_count = 0
check_str = 'UCPC'
for s in data:
    if s == check_str[check_count]:
        check_count += 1
        if check_count == 4:
            print('I love UCPC')
            exit()
print('I hate UCPC')
