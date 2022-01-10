data = [(lambda x:(x[0], int(x[1])))(input().split()) for _ in range(int(input()))]
print(' '.join([i[0] for i in sorted(data, key=lambda x:x[1])]))