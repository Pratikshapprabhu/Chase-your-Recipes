from django.contrib import admin
from django.urls import path,include
from .import views
from django.views.generic import RedirectView

app_name = "auth"
urlpatterns = [
    path('register/', views.register, name="register"),
    path("perform_register/",views.perform_register,name="perform_register"),
    path('render_login', views.render_login , name="render_login"),
    path("perform_login/",views.perform_login,name="perform_login"),
    path("perform_logout/",views.perform_logout,name="perform_logout"),
    ]
