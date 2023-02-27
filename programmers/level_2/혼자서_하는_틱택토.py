def check_win(board, target):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == target:
            return 1
        if board[0][i] == board[1][i] == board[2][i] == target:
            return 1
    if board[0][0] == board[1][1] == board[2][2] == target:
        return 1
    if board[0][2] == board[1][1] == board[2][0] == target:
        return 1
    return 0

def count_mark(board, type):
    ans = 0
    for i in range(3):
        ans += board[i].count(type)
    return ans

def solution(board):
    count_o = count_mark(board, 'O')
    count_x = count_mark(board, 'X')
    win_o = check_win(board, 'O') == 1
    win_x = check_win(board, 'X') == 1
    if win_o and win_x:
        return 0
    if win_o and count_x >= count_o:
        return 0
    if win_x and count_x < count_o:
        return 0
    if count_o - count_x < 0:
        return 0
    if abs(count_o - count_x) > 1:
        return 0
    if count_o + count_x == 9 and count_x > count_o:
        return 0
    return 1

print(solution(["O.X", ".O.", "..X"]) == 1)
print(solution(["OOO", "...", "XXX"]) == 0)
print(solution(["...", ".X.", "..."]) == 0)
print(solution(["...", "...", "..."]) == 1)
print(solution(["XXX", "OXO", "OOX"]) == 0)