from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('commonhome/', views.commonfun, name='common'),
]