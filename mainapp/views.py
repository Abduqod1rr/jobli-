from django.shortcuts import render ,HttpResponse
from django.views.generic import ListView ,CreateView ,UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from .models import Job , Apply
from django.urls import reverse_lazy
from users.models import CustomUser
# Create your views here.
def home(request):
    return HttpResponse("hello world")

class HomeView(LoginRequiredMixin,ListView):
    model=Job
    template_name='home.html'
    context_object_name='jobs'



class AddJobView(LoginRequiredMixin,CreateView):
    model=Job
    fields=['title','about']
    template_name='job_add.html'
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        # ownerni avtomatik login bo‘lgan user qilib qo‘yish
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class GetApply(LoginRequiredMixin,CreateView):
    model=Apply
    template_name='home.html'
    fields=[]
    success_url=reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.job_id=self.kwargs['pk']
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class ReadApply(LoginRequiredMixin, ListView,UserPassesTestMixin):
    model=Apply
    template_name='applies.html'
    context_object_name='apply'
    
    def test_func(self ,form):
        
        if Apply.objects.filter(user=self.request.user):
            return True