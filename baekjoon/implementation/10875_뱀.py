import sys
n = int(sys.stdin.readline().rstrip())
commands = []
for _ in range(int(input())):
    a, b = sys.stdin.readline().rstrip().split()
    commands.append((int(a), b))

dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
dir_num = 0
x = y = 0
if not commands or y + commands[0][0] > n:
    print(n + 1)
    exit()
hoz, ver = [(-n - 1, (-n - 1, n + 1)), (n + 1, (-n - 1, n + 1))], [((-n - 1, n + 1), -n - 1), ((-n - 1, n + 1), n + 1)]
hoz.append((x, (y, y + commands[0][0])))
y = y + commands[0][0]
sec = commands[0][0]

def set_direction(str, dir_num):
    if str == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        dir_num = (dir_num + 3) % 4
    return dir_num

dir_num = set_direction(commands[0][1], dir_num)
del commands[0]
def check(in_while):
    inf = int(1e9)
    global x, y, dir_num, sec
    # print(commands, x, y, dir_num, sec)
    if dir_num == 0: # hoz+ (0, 1)
        y += 1
        ny = y + (commands[0][0] - 1) * dir[dir_num][1] if in_while else n
        v_gap = h_gap = inf
        for v in ver:
            if v[0][0] <= x <= v[0][1] and y <= v[1] <= ny:
                v_gap = min(v_gap, v[1] - y + 1)
        for h in hoz:
            if h[0] == x and ny >= h[1][0] >= y:
                h_gap = min(h_gap, h[1][0] - y + 1)
        if v_gap != inf or h_gap != inf:
            print(min(sec + v_gap, sec + h_gap))
            exit()
        sec += commands[0][0] if in_while else n - y + 2
        hoz.append((x, (y - 1, ny)))
        y = ny
    elif dir_num == 1: # ver+ (1, 0)
        x += 1
        nx = x + (commands[0][0] - 1) * dir[dir_num][0] if in_while else n
        v_gap = h_gap = inf
        for h in hoz:
            if h[1][0] <= y <= h[1][1] and x <= h[0] <= nx:
                h_gap = min(h_gap, h[0] - x + 1)
        for v in ver:
            if v[1] == y and nx >= v[0][0] >= x:
                v_gap = min(v_gap, v[0][0] - x + 1)
        if v_gap != inf or h_gap != inf:
            print(min(sec + v_gap, sec + h_gap))
            exit()
        sec += commands[0][0] if in_while else n - x + 2
        ver.append(((x - 1, nx), y))
        x = nx
    elif dir_num == 2: # hoz- (0, -1)
        y -= 1
        ny = y + (commands[0][0] - 1) * dir[dir_num][1] if in_while else -n
        v_gap = h_gap = inf
        for v in ver:
            if v[0][0] <= x <= v[0][1] and ny <= v[1] <= y:
                v_gap = min(v_gap, y - v[1] + 1)
        for h in hoz:
            if h[0] == x and ny <= h[1][1] <= y:
                h_gap = min(h_gap, y - h[1][1] + 1)
        if v_gap != inf or h_gap != inf:
            print(min(sec + v_gap, sec + h_gap))
            exit()
        sec += commands[0][0] if in_while else y - -n + 2
        hoz.append((x, (ny, y + 1)))
        y = ny
    else: # ver- (-1, 0)
        x -= 1
        nx = x + (commands[0][0] - 1) * dir[dir_num][0] if in_while else n
        v_gap = h_gap = inf
        for h in hoz:
            if h[1][0] <= y <= h[1][1] and nx <= h[0] <= x:
                h_gap = min(h_gap, x - h[0] + 1)
        for v in ver:
            if v[1] == y and nx <= v[0][1] <= x:
                v_gap = min(v_gap, x - v[0][1] + 1)
        if v_gap != inf or h_gap != inf:
            print(min(sec + v_gap, sec + h_gap))
            exit()
        sec += commands[0][0] if in_while else x - -n + 2
        ver.append(((nx, x + 1), y))
        x = nx
    if in_while:
        dir_num = set_direction(commands[0][1], dir_num)
        del commands[0]
while commands:
    check(True)
check(False)
print(sec)