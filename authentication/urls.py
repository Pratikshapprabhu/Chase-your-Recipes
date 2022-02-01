from django.contrib import admin
from django.urls import path,include
from .import views
from django.views.generic import RedirectView

app_name = "auth"
urlpatterns = [
    path('register/', views.register, name="register"),
    path("perform_register/",views.perform_register,name="perform_register"),
    path('login', views.login , name="login"),
    path("perform_logout/",views.perform_logout,name="perform_logout"),
    ]
