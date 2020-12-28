from django.urls import path
from .views import *
urlpatterns = [
    path('login/', userlogin, name = 'userlogin'),
    path('logout/', userlogout, name='userlogout'),
    path('signup/', usersignup, name='usersignup'),
    path('', userdetails, name='userdetails'),
    path('useredit/',   useredit, name='useredit'),
    path('changePass/', changePass, name='changePass'),
]