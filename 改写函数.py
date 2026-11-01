#定义闰平年
def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
# #三个数比大小函数
def compare_size(a,b,c):
    if a >= b:
        biggest = a
    else:
        biggest = b
    if biggest >= c:
        return biggest
    else:
        return c
#猜大小

def b_or_s():
    import random
    answer = int(random.randint(1, 100))
    count = 0

    while True:
        a = input('猜一个 1-100 的数（输入 q 退出）：')
        if a == 'q':
            return count
        if not a.isdigit():
            print('请输入数字')
            continue
        count += 1
        if int(a) == answer:
            print(f'猜对了，你共用了{count}次')
            return count
        elif int(a) < answer:
            a = input('小了，请继续猜')
        elif int(a) > answer:
            a = input('大了，请继续猜')
if __name__ == "__main__":
    n =  b_or_s()
    print(f"游戏结束，共猜 {n} 次")


#输出菱形
def diamond(n):
    while True:
        if n % 2 == 0:
            return False
        else:
            break
    lines = []
    x = int((n + 1) / 2 + 1)
    for k in range(1, x):
        stars = 2 * k - 1
        spaces = int((n + 1) / 2 - k)
        line = ' ' * spaces + '*' * stars
        lines.append(line)
    for y in range(x, n + 1):
        stars = 2 * n - 2 * y + 1
        spaces = int(y - (n + 1) / 2)
        line = ' ' * spaces + '*' * stars
        lines.append(line)
    return '\n'.join(lines)
#average(nums) —— 算平均值
def average(nums):
    if len(nums) == 0:
        return None
    else:
        sum = 0
        count = 0
        for n in nums:
            sum += n
            count += 1
        return float(sum / count)
#count_char(s, ch) —— 数字符出现次数
def count_char(s,ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1
    return count

#to_int(text, default=0) —— 只接受「非负整数字符串」
def to_int(text, default=0):
    t=text.strip()
    if len(t) == 0 :
        return default
    if t.isdigit() :
        return int(t)
    else:
        return default




