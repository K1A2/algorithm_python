to = int(input())
memory = [0] * to
def fibo(n):
    if n == 1 or n == 2:
        memory[n - 1] = 1
        return 1
    elif memory[n - 1] != 0:
        return memory[n - 1]
    else:
        memory[n - 1] = fibo(n - 1) + fibo(n - 2)
        return memory[n - 1]
print(fibo(to))