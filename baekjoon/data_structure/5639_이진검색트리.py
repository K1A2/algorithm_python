import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
value = []
while 1:
    try:
        value.append(int(input()))
    except:
        break

def postorder(values):
    if len(values) == 1:
        print(values[0])
        return
    left = []
    right = []
    mid = values[0]
    for i in range(1, len(values)):
        if values[i] < mid:
            left.append(values[i])
        else:
            right.append(values[i])
    if len(left) > 0:
        postorder(left)
    if len(right) > 0:
        postorder(right)
    print(mid)
postorder(value)
