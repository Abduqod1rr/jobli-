from django.shortcuts import render ,HttpResponse
from django.views.generic import ListView ,CreateView ,UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job , Apply
# Create your views here.
def home(request):
    return HttpResponse("hello world")

class HomeView(LoginRequiredMixin,ListView):
    model=Job
    template_name='home.html'
    context_object_name='job'
 