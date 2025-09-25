from django.db import models
from users.models import CustomUser
# Create your models here.
class Job(models.Model):
    title=models.CharField(max_length=30)
    about=models.TextField()
    posted_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    
    class Meta():
        ordering=['-posted_at']

    def __str__(self):
        return f"{self.title} | {self.owner}"
    
class Apply(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    letter=models.TextField()
    applied_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.job