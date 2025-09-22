from django.contrib import admin
from django.urls import path ,include
from . import views
from users.views import UserRegister 
from django.contrib.auth.views import LoginView 


urlpatterns = [
    path('home/',views.HomeView.as_view(), name="home"),
    path('register/',UserRegister.as_view(),name='register'),
    path('login/',LoginView.as_view(template_name="login.html"),name="login"),
    path('job_add/',views.AddJobView.as_view(),name='job_add'),
    path('apply/<int:pk>',views.GetApply.as_view(),name='apply'),
    path('applies',views.ReadApply.as_view(),name='appies')
]
