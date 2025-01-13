d=[input(),input(),input()]
num = 0
for i in range(3):
    try:
        num = int(d[i])
        num += 3 - i
        break
    except:
        continue
if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0:
    print('Fizz')
elif num % 5 == 0:
    print('Buzz')
else:
    print(num)
