from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class users(models.Model):
    login_id = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    gender = models.CharField(max_length=1,default='M')
    description = models.TextField()
    profile_picture = models.ImageField()