from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup, name='SignUp'),
    path('login/',views.login,name='Login'),
    path('logout/',views.logout,name='Logout'),
]