from django.db import models

# Create your models here.
class registered_user(models.Model):
    username = models.CharField(max_length=25)
    emailid = models.EmailField()
    password = models.CharField(max_length=10)

