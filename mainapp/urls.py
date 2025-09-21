from django.contrib import admin
from django.urls import path ,include
from . import views
from users.views import UserRegister 
from django.contrib.auth.views import LoginView 


urlpatterns = [
    path('home/',views.home, name="home"),
    path('register/',UserRegister.as_view(),name='register'),
    path('login/',LoginView.as_view(template_name="login.html"),name="login")
]
