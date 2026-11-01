#8.12
# def make_sanwich(*args):
#     print(f'这是您要添加的辅料：{args}')
# make_sanwich(1, 2, 3)

#8.13
# def build_profile(first,last,**user_info):
#     user_info['first_name'] =first
#     user_info['last_name'] =last
#     return user_info
# user_profile=build_profile('chen','ye',location='ningbo',field='physics',age='35')
# print(user_profile)

#8.14
def make_cars(brand,model,**kwargs):
    kwargs["brand"] = brand
    kwargs["model"] = model
    return kwargs
car=make_cars('subaru','outback',color='blue',tow_package='True')
print(car)
