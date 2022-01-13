from django.contrib import admin

# Register your models here.
from .models import registered_user

admin.site.register(registered_user)
