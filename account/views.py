from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth


def checkSignMessage(request, user_name, pass_word, re_pass_word):
    try:
        User.objects.get(username=user_name)
        return render(request, 'signup.html', {'userError': '该用户已存在'})
    except User.DoesNotExist:
        if pass_word == re_pass_word:
            User.objects.create_user(username=user_name, password=pass_word)
            # return render(request, 'signup.html', {'Success': '账户成功创建'})
            return redirect('home')
        else:
            return render(request, 'signup.html', {'passwordError': '两次输入的密码不一致'})


# Create your views here

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == "POST":
            user_name = request.POST['user_name']
            pass_word = request.POST['password']
            re_pass_word = request.POST['re_password']
            return checkSignMessage(request, user_name, pass_word, re_pass_word)
            # try:
            #     User.objects.get(username=user_name)
            #     return render(request, 'signup.html', {'userError': '该用户已存在'})
            # except User.DoesNotExist:
            #     if pass_word == re_pass_word:
            #         User.objects.create_user(username=user_name, password=pass_word)
            #         # return render(request, 'signup.html', {'Success': '账户成功创建'})
            #         return redirect('home')
            #     else:
            #         return render(request, 'signup.html', {'passwordError': '两次输入密码错误'})


def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        user_name = request.POST['user_name']
        pass_word = request.POST['password']
        user=auth.authenticate(username=user_name,password=pass_word)
        if user==None:
            return render(request,'login.html',{'loginError':'账号或者密码有错'})
        else:
            auth.login(request,user)
            return redirect('home')


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')



