data = sorted([(int(input()), i) for i in range(8)], reverse=True)
print(sum([i[0] for i in data[:5]]))
print(*sorted([i[1] + 1 for i in data[:5]]))
