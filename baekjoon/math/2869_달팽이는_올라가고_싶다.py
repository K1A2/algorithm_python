a, b, v = list(map(int, input().split()))
answer = (v - b) // (a - b)
if (v - b) % (a - b) != 0:
    answer += 1
print(answer)