from collections import deque
def find(start, com, visited, n):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        now = q.popleft()
        for next_idx in range(n):
            if com[now][next_idx] and not visited[next_idx]:
                visited[next_idx] = True
                q.append(next_idx)
def solution(n, computers):
    answer = 0
    visited = [0] * n
    for x in range(n):
        if not visited[x]:
            find(x, computers, visited, n)
            answer += 1
    return answer
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2)
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1)