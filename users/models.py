from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES=(
        ("job seeker","Job seeker"),
        ("job owner","Job owner" ),
    )
    role=models.CharField(max_length=30, choices=ROLE_CHOICES, default="job seeker")
    
    def __str__(self):
        return f"{self.username} : {self.role}"