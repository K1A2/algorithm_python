memory = []
def padopan(n):
    if n == 0 or n == 1 or n == 2:
        memory[n] = 1
        return 1
    elif memory[n] != 0:
        return memory[n]
    else:
        memory[n] = padopan(n - 2) + padopan(n - 3)
        return memory[n]
for _ in range(int(input())):
    n = int(input())
    memory = [0] * n
    print(padopan(n - 1))