from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    

# Create your models here.

class UspsServices:
    id : int
    serviceName : str    
    serviceDescription : str    
    accessFlag : bool
    