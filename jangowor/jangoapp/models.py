from django.db import models


# Create your models here.
class Students(models.Model):
    student_name=models.CharField(max_length=20)
    rollnum=models.IntegerField()
    address=models.CharField(max_length=30,null=True)
    email=models.EmailField(max_length=25,null=True)