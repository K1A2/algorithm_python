n = int(input())

def print_first_last(n):
    print('*' * n, ' ' * (2 * (n - 2) + 1), '*' * n, sep='')

def print_body(n, reverse=False):
    for i in range(n - 2, 0, -1) if reverse else range(1, n - 1):
        print(' ' * i, '*', ' ' * (n - 2), '*', ' ' * (2 * (n - 2 - i) + 1), '*', ' ' * (n - 2), '*', sep='')

def print_middle(n):
    print(' ' * (n - 1), '*', ' ' * (n - 2), '*', ' ' * (n - 2), '*', sep='')

print_first_last(n)
print_body(n)
print_middle(n)
print_body(n, True)
print_first_last(n)
