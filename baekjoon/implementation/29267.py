n,k=map(int,input().split())
save = 0
now = 0
for _ in range(n):
    a=input()
    if a=='ammo':
        now += k
    elif a=='load':
        now = save
    elif a=='shoot' and now>0:
        now -= 1
    elif a=='save':
        save = now
    print(now)
