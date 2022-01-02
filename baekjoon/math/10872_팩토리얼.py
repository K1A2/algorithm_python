def facrotial(num, answer):
    if num <= 1:
        return answer
    else:
        return facrotial(num - 1, answer * num)
print(facrotial(int(input()), 1))