from django.db import models

# Create your models here.

class UserReg(models.Model):
    Name=models.CharField(max_length=30)
    Username=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
    Confirmpassword=models.CharField(max_length=30)
    Email=models.EmailField()
    Mobileno=models.IntegerField()
    Address=models.CharField(max_length=30)
    Resume=models.FileField(upload_to='FileUpload/')

    def __str__(self):
        return self.Username
