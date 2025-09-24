from django.db.models.query import QuerySet
from django.shortcuts import render ,HttpResponse
from django.views.generic import ListView ,CreateView ,UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from .models import Job , Apply
from django.urls import reverse_lazy
from users.models import CustomUser
from typing import Optional, cast
# Create your views here.
def home(request):
    return HttpResponse("hello world")

class HomeView(LoginRequiredMixin,ListView):
    model=Job
    template_name='home.html'
    context_object_name='jobs'

    def search(self):
        query=self.request.GET.get('q')
        if query:
            return Job.objects.filter(title__icontains=query)
        return Job.objects.all()
    
    def get_queryset(self):
        return self.search()

#DELETE 
class DeleteJob(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Job
    template_name='job_delete.html'
    success_url=reverse_lazy('home')

    def test_func(self) :
        job=cast(Job,self.get_object())
        return job.owner == self.request.user

#UPDATE
class UpdateJob(LoginRequiredMixin , UserPassesTestMixin ,UpdateView,CustomUser):
    model = Job
    
    success_url=reverse_lazy('home')

    def test_func(self) :
        job = cast(Job,self.get_object())
        return job.owner == self.request.user


class ViewMyJobs(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model=Job
    template_name='myjobs.html'
    context_object_name='jobs'

    def get_queryset(self):
        return Job.objects.filter(owner=self.request.user)
   
    def test_func(self) :
        return self.request.user.is_authenticated

class AddJobView(LoginRequiredMixin, UserPassesTestMixin,CreateView ):
    model=Job
    fields=['title','about']
    template_name='add_job.html'
    success_url=reverse_lazy('home')

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        user=cast(CustomUser,self.request.user)
        return user.role=='Job owner' 

    def form_valid(self, form):
        
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class GetApply(LoginRequiredMixin,CreateView):
    model=Apply
    template_name='home.html'
    fields=[]
    success_url=reverse_lazy('home')

    class Meta:
        unique_together=('job','user')
    
    def form_valid(self, form):
        form.instance.job_id=self.kwargs['pk']
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class ReadApply(LoginRequiredMixin, ListView,UserPassesTestMixin):
    model=Apply
    template_name='applies.html'
    context_object_name='apply'
    
    def get_queryset(self) :
        return Apply.objects.filter(job__owner=self.request.user)