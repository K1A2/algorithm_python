def solution(triangle):
    for x in range(len(triangle) - 2, -1, -1):
        for y in range(len(triangle[x])):
            triangle[x][y] += max(triangle[x + 1][y], triangle[x + 1][y + 1])
    return triangle[0][0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))