n, l = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]


def count(mode=0):
    # print('mode', mode)
    ans = 0
    for i in range(n):
        if mode:
            last_highest = data[0][i]
        else:
            last_highest = data[i][0]
        continuous = 1
        end = 0
        is_ans = 1
        for j in range(1, n):
            now = data[j][i] if mode else data[i][j]
            prev = data[j - 1][i] if mode else data[i][j - 1]
            if now == prev:
                continuous += 1
                if last_highest - now == 1:
                    if continuous == l:
                        continuous = 0
                        last_highest = now
                    else:
                        if j == n - 1: end = 1
                elif last_highest - now >= 2:
                    is_ans = 0
                    break
            elif now == prev + 1:
                if continuous >= l:
                    last_highest = now
                    continuous = 1
                else:
                    is_ans = 0
                    break
            elif now == prev - 1:
                continuous = 1
                if continuous == l:
                    continuous = 0
                    last_highest = now
                else:
                    if j == n - 1: end = 1
            else:
                is_ans = 0
                break
        if end:
            # print('end', i, continuous)
            if continuous < l:
                continue
        if is_ans:
            # print(i)
            ans += 1
    return ans


print(count(0) + count(1))
