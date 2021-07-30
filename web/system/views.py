from django.shortcuts import render,HttpResponse,redirect,reverse
from system.models import Account
from functools import wraps
from django.contrib import messages
# Create your views here.


# 利用函数修饰器完成登录状态的判断
def is_login(func):
    '''
    判断是否在登录状态，通过session判断，Session对象存储特定用户会话所需的属性及配置信息。
    :param func:
    :return:
    '''
    @wraps(func)
    def wrapper(request,*args,**kwargs):
        # 获取用户信息
        user = request.session.get('user',None)
        if user:
            return func(request,*args,**kwargs)
        else:
            messages.error(request,'用户未登录,请先登录')
            return redirect(reverse('login'))
    return wrapper

def login(request):
    if request.method == 'POST':
        # 获取输入的id和password
        username = request.POST['username']
        password = request.POST['password']
        # 获取数据库中的对象
        account = Account.objects.filter(email=username).first()
        if account:
            true_password = account.password
            if true_password == password:
                messages.info(request,'登录成功')
                # 密码正确，复制给session
                print('密码正确')
                request.session['username'] = username
                # 设置三百分钟内有效
                request.session.set_expiry(60 * 300)
                return redirect(reverse('index'))
            else:
                messages.error(request, "用户名或密码不正确！")
                return redirect(reverse('login'))
        else:
            messages.info(request, "用户不存在！")
            return redirect(reverse('login'))

    return render(request,'system/login.html')


def logout(request):
    return HttpResponse('退出')


# @is_login
def index(request):
    return render(request,'base.html')
