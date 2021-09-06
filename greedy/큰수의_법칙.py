n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

big_1 = data[n - 1]
big_2 = data[n - 2]

result = big_1 * k * (m // k) + big_2 * (m % k)
print(result)