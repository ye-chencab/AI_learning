# number = 1
# sum_0 = 0
# while number <= 100:
#     sum_0 += number
#     number += 1
# print(sum_0)
import numbers

#判断闰年
# year = int(input("请输入你要查询的年份"))
# if year % 4 == 0 and year % 100 != 0 :
#     print("闰年")
# elif year % 400 == 0:
#             print("闰年")
# else:
#                 print("平年")
#三个数，比大小
# numbers = []
# number =''
# while True:
#     number = input("请依次输入三个数，输入'Q'结束：")
#     if number == "Q":
#         break
#     numbers.append(number)
# number_1 = int(numbers.pop())
# number_2 = int(numbers.pop())
# number_3 = int(numbers.pop())
# if number_1 > number_2:
#     the_biggist=number_1
# else:
#     the_biggist=number_2
# if the_biggist > number_3:
#     print(f'最大的数是{the_biggist}')
# else:
#     print(f'最大的数是{number_3}')

#猜大小
# count = 0
# number_1 = input('猜一个1-100的数，直到猜对，或输入“不猜了”为止：')
# while True:
#     count += 1
#     if int(number_1) > 15:
#         print('大了')
#     elif int(number_1) < 15:
#         print('小了')
#     elif int(number_1) == 15 or number_1 == '不猜了':
#         print(f'猜对了，你共用了{count}次')
#         break
#     number_1 = int(input('猜一个1-100的数，直到猜对，或输入“不猜了”为止：'))

#输出菱形：输入一个奇数 n，打印一个 n 行的菱形
n = int(input('请输入一个奇数'))
while True:
    if n % 2 == 0:
        n = int(input('请输入一个奇数：'))
    else:
        break
x = int((n+1)/2+1)
for k in range(1 , x):
        stars = 2 * k -1
        spaces = int((n+1)/2 - k)
        print(' ' * spaces + '*' * stars)
for y in range(x , n+1):
        stars = 2*n - 2*y + 1
        spaces = int(y - (n+1)/2)
        print(' ' * spaces + '*' * stars)


