from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('login',views.sel_loginfun, name='login'),
    path('signup',views.sel_signupfun, name='signup'),
    path('master', views.sel_masterfun, name='s_master'),
    path('seller_home',views.sel_homefun, name='sel_home'),
    path('seller_loghome',views.sel_loghome, name='sel_loghome'),
    path('addproduct',views.sel_addproduct, name='addproduct'),
    path('profile',views.sel_profile, name='profile'),
    path('myProducts',views.sel_myproducts, name='myProducts'),
    path('changePassword',views.sel_changePassword, name='changePassword'),
    path('editProfile',views.sel_editProfile, name='editProfile'),
    path('logout',views.sel_logout, name='logout'),
]