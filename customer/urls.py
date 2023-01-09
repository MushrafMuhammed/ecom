from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('login', views.cus_loginfun, name='login'),
    path('signup', views.cus_signupfun, name='signup'),
    path('master', views.cus_masterfun, name='master'),
    path('products', views.cus_productsfun, name='products'),
    path('myorder', views.cus_orderfun, name='myorder'),
    path('changepassword', views.cus_changepasswordfun, name='chgpassword'),
    path('profile', views.cus_profilefun, name='profile'),
    path('support', views.cus_supportfun, name='support'),
    path('logout', views.cus_logoutfun, name='logout'),
   
]