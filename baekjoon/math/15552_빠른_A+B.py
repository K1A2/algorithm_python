from sys import stdin
for _ in range(int(stdin.readline())):
    print(sum(map(int, stdin.readline().rstrip().split())))