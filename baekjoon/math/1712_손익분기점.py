money = input().split()
fixed = int(money[0])
make = int(money[1])
price = int(money[2])

if make >= price:
    print(-1)
else:
    print(int(fixed/(price-make)) + 1)