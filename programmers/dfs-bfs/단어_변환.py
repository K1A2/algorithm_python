def dfs(now, target, words, used, count, asw):
    for idx_w, w in enumerate(words):
        if idx_w in used:
            continue
        diff = 0
        for idx, n in enumerate(now):
            if n != w[idx]:
                diff += 1
        if diff == 1:
            if w == target:
                return min(count + 1, asw)
            asw = dfs(w, target, words, used + [idx_w], count + 1, asw)
    return asw

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    return dfs(begin, target, words, [], 0, 51)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))