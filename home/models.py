from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Custom_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    father = models.CharField(max_length=1000)
    address = models.TextField()
    dob = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    marks = models.IntegerField(default=0)
