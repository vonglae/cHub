from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PRODUCT
from django.utils import timezone


# Create your views here.

def products_list(request):
    return render(request, 'product_list.html')


@login_required
def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    elif request.method == 'POST':
        product_name = request.POST['product_name']
        introduction = request.POST['introduction']
        product_linked = request.POST.get('product_linked')
        icon = request.FILES.get('icon')
        # dict.get()方法如果没有这个key会返回一个none而request.POST[]会返回一个错误
        picture = request.FILES.get('picture')
        # icon = request.FILES['icon']
        # picture = request.FILES['picture']
        print(picture)
        print(icon)

        if icon and picture is not None:
            # None在Python里是个单例对象，一个变量如果是None，它一定和None指向同一个内存地址。None是python中的一个特殊的常量，表示一个空的对象。空值是Python中的一个特殊值，数据为空并不代表是空对象，
            # 例如[]，''，()，{}
            # 等都不是None
            product = PRODUCT()
            print('ok')
            product.product_name = product_name
            product.introduction = introduction
            product.product_linked = product_linked
            product.icon = icon
            product.picture = picture
            product.product_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('home')
        else:
            return render(request, 'publish.html', {'imageError': '没有上传图标或者产品全图'})

