n = int(input())
def print_star(n, reverse=False):
    for i in range(n - 1, 0, -1) if reverse else range(1, n):
        print('*' * i, ' ' * (2 * (n - i)) , '*' * i, sep='')

print_star(n)
print('*' * (2 * n))
print_star(n, True)
