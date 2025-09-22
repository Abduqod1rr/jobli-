from django.db import models
from users.models import CustomUser
# Create your models here.
class Job(models.Model):
    title=models.CharField(max_length=30)
    about=models.TextField()
    posted_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.title,self.owner