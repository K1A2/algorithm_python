def get_part(tabe, start):
    pass

def solution(game_board, table):
    answer = -1
    return answer

testcase = [
    (([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
      [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]), 14),
    (([[0,0,0],[1,1,0],[1,1,1]],
      [[1,1,1],[1,0,0],[0,0,0]]), 0),
]

if __name__ == '__main__':
    for idx, t in enumerate(testcase):
        print(f'{idx}번째: {solution(t[0], t[1]) == t[-1]}')