from django.contrib import admin
from django.urls import path,include
from . import  views

urlpatterns = [
    path('', views.products_list, name='home' ),
    path('publish/',views.publish,name='Publish'),
    path('<int:product_id>/',views.detail,name='Detail'),
]
