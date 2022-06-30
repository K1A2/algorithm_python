p = 15 * (10 ** 5)
m = 10 ** 6
n = int(input()) % p
fibo = [0] * p
fibo[1] = 1
for i in range(2, p):
    fibo[i] = (fibo[i - 1] + fibo[i - 2]) % m
print(fibo[n])