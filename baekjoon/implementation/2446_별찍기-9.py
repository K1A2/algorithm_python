n = int(input())
def print_star(n, reverse=False):
    for i in range(n, 0, -1) if reverse else range(1, n):
        print(' ' * (i - 1), '*' * (2 * (n - i) + 1), sep='')

print_star(n)
print_star(n, True)
