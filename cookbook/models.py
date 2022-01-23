from email.policy import default
from django.db import models

# Create your models here.
class RecipeStore(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255, primary_key=False)
    ingredients = models.TextField(max_length=10240)
    preparation = models.TextField(max_length=10240)
    desc = models.TextField(max_length=10240)
    #tags = models.CharField(max_length=10)

    def __str__(self):
        return self.url


class RecipeIndex(models.Model):
    id = models.OneToOneField(RecipeStore, on_delete=models.CASCADE,primary_key=True)
    recipe_name = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)

    def __str__(self):
        return self.recipe_name