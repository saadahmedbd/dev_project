from django.db import models

# Create your models here.
class Record (models.Model):
    creation_date =models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=30)

    last_name =models.CharField(max_length=30)

    email = models.CharField(max_length=50)

    phone =models.CharField(max_length=20)

    city = models.CharField(max_length=30)

    country =models.CharField(max_length=30)

def __str__(self):
    return self.first_name +"   "+self.last_name


    

    
