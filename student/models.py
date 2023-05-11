from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    student_id = models.IntegerField()
    email = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    def __str__(self):
        return self.name
    
