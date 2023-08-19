from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length = 50)
    mobile = models.IntegerField()
    skill = models.CharField(max_length=20)
    city = models.CharField(max_length=15)