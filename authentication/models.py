from django.db import models
from django.contrib.auth.models import AbstractUser
from cookbook.models import RecipeIndex

class CustomUser(AbstractUser):
    recipes = models.ManyToManyField(RecipeIndex, blank=True)

    def __str__(self):
        return self.username
