n = 9
height = sorted([int(input()) for _ in range(n)], reverse=True)
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            for l in range(k + 1, n):
                for m in range(l + 1, n):
                    for o in range(m + 1, n):
                        for p in range(o + 1, n):
                            if height[i] + height[j] + height[k] + height[l] + height[m] + height[o] + height[p] == 100:
                                print(' '.join([str(height[z]) for z in [p, o, m, l, k, j, i]]))
                                exit()