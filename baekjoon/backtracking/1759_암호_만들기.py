import sys
input = sys.stdin.readline
l, c = map(int, input().rstrip().split())
words = sorted(input().rstrip().split())
vowels = set(['a', 'e', 'i', 'o', 'u'])
def backtracking(v_count, count, start, result):
    if count == l:
        if v_count > 0 and count - v_count > 1:
            print(''.join(result))
        return
    for i in range(start, c):
        result.append(words[i])
        backtracking(v_count + (1 if words[i] in vowels else 0), count + 1, i + 1, result)
        result.pop()
backtracking(0, 0, 0, [])