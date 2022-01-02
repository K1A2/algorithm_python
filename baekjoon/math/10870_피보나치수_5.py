def fibonachi(now, answer, prev, prev2, limit):
    if now >= limit:
        return answer
    else:
        return fibonachi(now + 1, prev + prev2, prev + prev2, prev, limit)

i = int(input())
if i <= 1:
    print(i)
else:
    print(fibonachi(2, 1, 1, 1, i))