n = int(input())
def print_star(n, reverse=False):
    for i in range(1, n) if reverse else range(n - 1, -1, -1):
        print(' ' * i, '*' * (n - i), sep='')
print_star(n)
print_star(n, True)