from django.shortcuts import render


# Create your views here.

def products_list(request):

    return render(request,'product_list.html')