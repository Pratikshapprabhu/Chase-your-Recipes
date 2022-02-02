from django.contrib import admin
from django.contrib.auth import views as dviews
from django.urls import path,include
from .import views
from django.views.generic import RedirectView

app_name = "auth"
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login', dviews.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', dviews.LogoutView.as_view(template_name="logout.html"), name="logout"),
    ]
