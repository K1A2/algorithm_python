def binary(n):
    res = []
    while n > 1:
        res.append(n % 2)
        n //= 2
    res.append(n)
    res.reverse()
    return ''.join(list(map(str, res)))

def solution(s):
    count_proc = zeros = 0
    while s != '1':
        ones = s.count('1')
        count_proc += 1
        zeros += len(s) - ones
        s = binary(ones)
    return [count_proc, zeros]

print(solution('110010101001') == [3,8])
print(solution('01110') == [3,3])
print(solution('1111111') == [4,1])