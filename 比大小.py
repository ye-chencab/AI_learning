#三个数，比大小
while True:
    a = input('请输入第一个数：')
    if a.title() == 'Q' :
        break
    b = input('请输入第二个数：')
    if b.title() == 'Q' :
        break
    c = input('请输入第三个数：')
    if c.title() == 'Q' :
        break
    if int(a) > int(b):
        the_biggist = a
    else:
        the_biggist = b
    if int(the_biggist) > int(c):
        print(f'最大的数是 {the_biggist} 。')
    else:
        print(f'最大是数是{c}')


