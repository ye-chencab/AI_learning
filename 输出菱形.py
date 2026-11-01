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

