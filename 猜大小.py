#猜大小
import random
count = 0
number = random.randint(1, 100)
number_1 = input('猜一个1-100的数，直到猜对，或输入“不猜了”为止：')
while True:
    if  number_1 == '不猜了':
        break
    count += 1
    if int(number_1) > number:
        print('大了')
    elif int(number_1) < number:
        print('小了')
    elif int(number_1) == number :
        print(f'猜对了，你共用了{count}次')
        break
    number_1 = input('猜一个1-100的数，直到猜对，或输入“不猜了”为止：')
