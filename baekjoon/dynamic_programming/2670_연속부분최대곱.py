n = int(input())
data = [float(input()) for _ in range(n)]
for i in range(1, n):
    data[i] = max(data[i], data[i] * data[i - 1])
print("%0.3f" % max(data))
