from django.db import models

# Create your models here.
#importing USER bulit in model
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField(max_length=200)
    profile_pic=models.ImageField(upload_to='profile_pic')

