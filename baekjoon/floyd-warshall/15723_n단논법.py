import sys
input = sys.stdin.readline
alphabet_len = 26
data = [[sys.maxsize] * alphabet_len for _ in range(alphabet_len)]
for _ in range(int(input())):
    a, b = map(lambda x: ord(x) - ord('a'), input().rstrip().split(' is '))
    data[a][b] = 1
for k in range(alphabet_len):
    for i in range(alphabet_len):
        for j in range(alphabet_len):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])
for _ in range(int(input())):
    a, b = map(lambda x: ord(x) - ord('a'), input().rstrip().split(' is '))
    if data[a][b] != sys.maxsize:
        print('T')
    else:
        print('F')
