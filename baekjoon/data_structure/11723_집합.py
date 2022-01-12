import sys
data = set()
for _ in range(int(sys.stdin.readline().rstrip())):
    com = sys.stdin.readline().rstrip().split()
    if com[0] == 'add':
        data.add(int(com[1]))
    elif com[0] == 'remove':
        if int(com[1]) in data:
            data.remove(int(com[1]))
    elif com[0] == 'check':
        if int(com[1]) in data:
            print(1)
        else:
            print(0)
    elif com[0] == 'toggle':
        if int(com[1]) in data:
            data.remove(int(com[1]))
        else:
            data.add(int(com[1]))
    elif com[0] == 'all':
        data = set([i for i in range(1, 21)])
    else:
        data = set()