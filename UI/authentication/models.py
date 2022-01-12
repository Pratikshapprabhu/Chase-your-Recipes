from django.db import models

# Create your models here.
class registered_user(models.Model):
    username = models.CharField(max_length=25)
    emailid = models.EmailField(max_length=50)
    password = models.CharField(max_length=10)

