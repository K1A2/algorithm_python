import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    number_max = list('1' * (n // 2))
    if n % 2: number_max[0] = '7'
    if n < 11:
        number_min = ['0', '0', '1', '7', '4', '2', '6', '8', '10', '18', '22'][n]
    else:
        number_min = list('8' * ((n + 6) // 7))
        if n % 7 == 1:
            number_min[0] = '1'
            number_min[1] = '0'
        elif n % 7 == 2:
            number_min[0] = '1'
        elif n % 7 == 3:
            number_min[0] = '2'
            number_min[1] = number_min[2] = '0'
        elif n % 7 == 4:
            number_min[0] = '2'
            number_min[1] = '0'
        elif n % 7 == 5:
            number_min[0] = '2'
        elif n % 7 == 6:
            number_min[0] = '6'
        number_min = ''.join(number_min)
    print(number_min, ''.join(number_max))
