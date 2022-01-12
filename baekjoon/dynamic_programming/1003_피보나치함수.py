check = [[] for _ in range(41)]
check[0] = [1,0]
check[1] = [0,1]
def fibo(n):
    if check[n]:
        return check[n]
    else:
        a, b = fibo(n - 1), fibo( n - 2)
        check[n] = [a[0] + b [0], a[1] + b [1]]
        return check[n]
for _ in range(int(input())):
    n = int(input())
    if n < 2:
        print(' '.join([str(i) for i in check[n]]))
        continue
    print(' '.join([str(i) for i in fibo(n)]))