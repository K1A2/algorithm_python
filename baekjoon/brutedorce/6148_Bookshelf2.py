from itertools import combinations
N, B = map(int, input().split())
heights = [int(input()) for _ in range(N)]

min_excess = float('inf')
for i in range(1, N + 1):
    for comb in combinations(heights, i):
        total_height = sum(comb)
        if total_height >= B:
            excess = total_height - B
            if excess < min_excess:
                min_excess = excess
print(min_excess)
