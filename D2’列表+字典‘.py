#字典存「姓名 → 电话」，菜单循环，支持 5 个功能
contacts ={'chen':'123548','zheng':'12876754'}
def contact_d():
    while True:
        a = input('请选择您要使用的功能：1 添加 2 查询 3 删除 4 列出全部 5 推出')
        if not a.isdigit():
            continue
        if int(a) == 1:
                name = input('请输入你要存入的姓名')
                tel = input('请输入电话')
                contacts[name] = tel
                print('已存入')
        elif int(a) == 2:
                k = input('请输入你要查询的姓名')
                print(contacts.get(k,'查无此人'))
        elif int(a) == 3:
            k = input('请输入你要删除的姓名')
            if k in contacts:
                del contacts[k]
            else:
                print('查无此人')
        elif int(a) == 4:
            if contacts :
                for name , tel in contacts.items():
                    print(f'{name},{tel}')
            else:
                print('通讯录已空')
        elif int(a) == 5:
                print('谢谢使用')
                break
        else:
                print('输入有误')

if __name__ == '__main__':
    contact_d()
contact_d(1)
#统计字符串里每个字符出现的次数，返回字典
def char_count(s):
    d  = {}
    for ch in s:
        d[ch] = d.get(ch,0) + 1
    return d


#列表去重，保持原顺序
def unique(nums):
    result = []
    for i in nums:
        if i not in result:
            result.append(i)
    return result
#返回列表中第二大的不同值
def second_max(nums):
    if len(nums) <= 1:
        return None
    else:
        a = None
        b = None
        for i in range(0,len(nums)):
            if a is None or nums[i] > a:
                b = a
                a = nums[i]
            elif nums[i] != a (b is None or nums[i] > b):
                b = nums[i]
        return b


#合并两个字典，键冲突时以 b 为准，且不能修改原来的 a、b
def merge(a,b):
    a_1 =a.copy()
    a_1.update(b)
    return a_1
