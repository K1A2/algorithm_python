from collections import deque
dir = ((-1, 0), (0, 1), (1, 0), (0, -1))
def bfs(x, y, visited, visited_id, room):
    q = deque()
    q.append((x, y, 0))
    while q:
        x, y, distance = q.popleft()
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] != visited_id:
                if room[nx][ny] == 'P':
                    if distance < 2:
                        return 0
                elif room[nx][ny] == 'O':
                    q.append((nx, ny, distance + 1))
                    visited[nx][ny] = visited_id
    return 1
def solution(places):
    answer = []
    n = 5
    for place in places:
        room = [list(i) for i in place]
        visited = [[0] * n for _ in range(n)]
        visited_id = 1
        result = 1
        for x in range(n):
            for y in range(n):
                if room[x][y] == 'P' and not visited[x][y]:
                    visited[x][y] = visited_id
                    result = bfs(x, y, visited, visited_id, room)
                    visited_id += 1
                    if not result:
                        answer.append(result)
                        break
            if not result:
                break
        if result:
            answer.append(result)
    return answer
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]) == [1, 0, 1, 1, 1])
print(solution([["OOPOO", "OOOOO", "OPOPO", "OOOOO", "OOOOO"]]) == [0])