# 猜大小
# import random
# count = 0
# number = random.randint(1, 100)
# while True:
#     number_1 = input('猜一个1-100的数，直到猜对，或输入“不猜了”为止：')
#     if  number_1 == '不猜了':
#         break
#     try:
#         number_1 = int(number_1)
#     except ValueError:
#         number_1 = input('请输入整数')
#         continue
#     count += 1
#     if number_1 > number:
#         print('大了')
#     elif number_1 < number:
#         print('小了')
#     elif number_1 == number :
#         print(f'猜对了，你共用了{count}次')
#         break
# import 改写函数
# print(改写函数.leap_year(1900))
# print(改写函数.to_int("  42 "))
def read_int(prompt):
    while True:
        try:
            a = int(input(prompt))
            return a
        except ValueError:
            prompt = input('请输入整数')

try:
    with open('data.txt') as f:
        content = f.read()
except FileNotFoundError:
    print('要打开的文件未找到')



def read_sorce(grades):
    bad = 0
    sorces = []
    try:
        with open(grades,'r',encoding='utf-8' ) as f:
                for line in f :
                    line = line.strip()
                    if not line:
                        continue
                    line = line.split(',')
                    if len(line) != 2:
                        bad += 1
                        continue
                    else:
                        try:
                            sorce = int(line[1])
                        except ValueError:
                            bad += 1
                            continue
                        sorces.append((line[0],sorce))
    except FileNotFoundError:
        print('文件未找到')
        return [],0
    return sorces,bad
print(read_sorce("测试文件"))





