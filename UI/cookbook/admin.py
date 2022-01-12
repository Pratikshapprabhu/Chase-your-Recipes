from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import RecipeIndex, RecipeStore
# Register your models here.
admin.site.register(RecipeIndex)
admin.site.register(RecipeStore)
