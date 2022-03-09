from email import message
from unicodedata import category
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.

class Custom_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    father = models.CharField(max_length=1000)
    address = models.TextField()
    dob = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    marks = models.IntegerField(default=0)

category_subject = (
    ("1", "Choice a subject"),
    ("English", "English"),
    ("Math", "Math"),
    ("Physics", "Physics"),
    ("Chemistry", "Chemistry"),
    ("Computer", "Computer"),
)

class Questions(models.Model):
    id_no = models.AutoField(primary_key=True, unique=True)
    category = models.CharField(max_length = 20, choices = category_subject, default = '1')
    question = models.CharField(max_length=10000)
    option_a = models.CharField(max_length=1000)
    option_b = models.CharField(max_length=1000)
    option_c = models.CharField(max_length=1000)
    option_d = models.CharField(max_length=1000)
    correct = models.CharField(max_length=1000)