from collections import deque

def sort_point(part):
    return sorted(part, key=lambda x: (x[0], x[1]))

def move_origin(part):
    top_x = min([i[0] for i in part])
    left_y = min([i[1] for i in part])
    return list(map(lambda x: (x[0] - top_x, x[1] - left_y), part))

def rotate_part(part):
    max_x = max([i[0] for i in part])
    max_y = max([i[1] for i in part])
    n = max(max_x, max_y)
    new_part = []
    for p in part:
        new_part.append((p[1], n - p[0]))
        # new_table[j][n - i] = part[i][j]
    new_part = move_origin(new_part)
    return new_part

def get_part(table, start_x, start_y, target):
    dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))
    len_table = len(table)
    q = deque()
    q.append((start_x, start_y))
    part_points = [(start_x, start_y)]
    table[start_x][start_y] = int(not bool(target))
    while q:
        x, y = q.popleft()
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < len_table and 0 <= ny < len_table and table[nx][ny] == target:
                part_points.append((nx, ny))
                q.append((nx, ny))
                table[nx][ny] = int(not bool(target))
    part_points = move_origin(part_points)
    return sort_point(part_points)

def find_part(board, part):
    count = 0
    used = [0] * len(part)
    for b in board:
        for idx, p in enumerate(part):
            if used[idx]: continue
            for _ in range(4):
                # print(b, p)
                if b == p:
                    count += len(p)
                    used[idx] = 1
                    break
                p = sort_point(rotate_part(p))
            if used[idx]: break
            # print(b, p)
        # print()
    return count

def solution(game_board, table):
    len_table = len(table)
    parts = []
    board_shape = []
    for i in range(len_table):
        for j in range(len_table):
            if table[i][j]:
                parts.append(get_part(table, i, j, 1))
            if not game_board[i][j]:
                board_shape.append(get_part(game_board, i, j, 0))
    parts.sort(key=lambda x: len(x))
    board_shape.sort(key=lambda x: len(x))
    # print(board_shape)
    # print(parts)
    answer = find_part(board_shape, parts)
    # print(answer)
    return answer

testcase = [
    (([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
      [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]), 14),
    (([[0,0,0],[1,1,0],[1,1,1]],
      [[1,1,1],[1,0,0],[0,0,0]]), 0),
    (([[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]],
      [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]), 54),
]

if __name__ == '__main__':
    for idx, t in enumerate(testcase):
        print(f'{idx}번째: {solution(t[0][0], t[0][1]) == t[-1]}')