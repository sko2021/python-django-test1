from django.db import models

# Create your models here.

class UspsServices (models.Model):
#    id : int
    serviceName = models.CharField(max_length=1000)
    serviceDescription = models.TextField()    
    accessFlag = models.BooleanField(default=False)
