
#判断闰年
year = int(input("请输入你要查询的年份"))
if year % 4 == 0 and year % 100 != 0 :
    print("闰年")
elif year % 400 == 0:
            print("闰年")
else:
                print("平年")



