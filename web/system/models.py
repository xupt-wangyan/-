from django.db import models

# create a account model
# 系统只需要一个管理员账号即可
'''
登录时通过邮箱或者id验证
'''
class Account(models.Model):
    # 用户邮箱，该邮箱用于对管理员的账号验证
    email = models.EmailField()
    # 用户密码
    password = models.CharField(max_length=200)
    # 用户真实姓名
    name = models.CharField(max_length=40)
    # 用户id
    id_man = models.CharField(max_length=40)
