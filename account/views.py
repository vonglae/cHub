from django.shortcuts import render
from django.contrib.auth.models import User


def checkSignMessage(request, user_name, pass_word, re_pass_word):
    try:
        User.objects.get(username=user_name)
        return render(request, 'signup.html', {'userError': '该用户已存在'})
    except User.DoseNotExist:
        if pass_word == re_pass_word:
            User.objects.create_user(username=user_name, password=pass_word)
            return render(request, 'signup.html', {'Success': '账户成功创建'})
        else:
            return render(request, 'signup.html', {'passwordError': '两次输入密码错误'})


# Create your views here

def signup(request):
    if request.method == 'GET' or 'get':
        return render(request, 'signup.html')
    elif request.method == "POST" or 'post':
            user_name = request.POST['user_name']
            pass_word = request.POST['password']
            re_pass_word = request.POST['re_password']
            print(user_name,pass_word,re_pass_word)
            print('hello world')
            checkSignMessage(request, user_name, pass_word, re_pass_word)
        # try:
        #     User.objects.get(username=user_name)
        #     return render(request, 'signup.html', {'userError': '该用户已存在'})
        # except User.DoesNotExist:
        #     if pass_word == re_pass_word:
        #         User.objects.create_user(username=user_name, password=pass_word)
        #         return render(request, 'signup.html', {'Success': '账户成功创建'})
        #     else:
        #         return render(request, 'signup.html', {'passwordError': '两次输入密码错误'})
