from django.shortcuts import render , redirect
from django.contrib.auth.views import LoginView ,LogoutView 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
# Create your views here.
class UserRegister(CreateView):
    model=CustomUser
    template_name='register.html'
    fields=['username','password','role']
    success_url=reverse_lazy("login")

    def form_valid(self, form):
        form.instance.password = make_password(form.instance.password)
        
        return super().form_valid(form)
    

