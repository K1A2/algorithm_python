n=int(input())
m=int(input())
for i in range(0, 100):
    nn=int(str(n)[:-2]+str(i).zfill(2))
    if nn%m==0:
        print(str(i).zfill(2))
        break