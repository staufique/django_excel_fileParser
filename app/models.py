from django.db import models

# Create your models here.

class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100)
    age = models.TextField(max_length=100)
    roll_no=models.TextField(max_length=100)
    mobile_no = models.IntegerField()
    email = models.EmailField()
    city = models.TextField(max_length=100)
    state = models.TextField(max_length=100)
    
class AdditionalInfo(models.Model):
    id=models.AutoField(primary_key=True)
    fathers_name=models.TextField(max_length=100)
    f_mobile=models.TextField(max_length=100)
    f_email = models.TextField(max_length=100)
    f_age=models.IntegerField()