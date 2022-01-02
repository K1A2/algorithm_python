for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    distance = y - x - 2
    if distance <= 1:
        print(distance + 2)
    elif 2 <= distance  <= 3:
        print(distance + 1)
    else:
        count = 1
        answer = 2
        while True:
            n = count * (count + 3)
            if n >= distance:
                if n == distance:
                    answer += count * 2
                    break
                nam = distance - ((count - 1) * (count + 2))
                if nam <= count:
                    answer += (count - 1) * 2 + 1
                    break
                nam = nam - count - 1
                if 0 < nam <= count + 1:
                    answer += count * 2
                    break
                else:
                    answer += (count - 1) * 2 + 1
                    break
            count += 1
        print(answer)