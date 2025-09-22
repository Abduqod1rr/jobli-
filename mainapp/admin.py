from django.contrib import admin
from .models import Job
from users.models import CustomUser

# Register your models here.
admin.site.register(Job)
admin.site.register(CustomUser)