from  django.urls import  path
from  . import views

urlpatterns = [
    path('', views.Login, name='login'), 
    path('login_user/', views.login_user, name='login_user'),
]




    