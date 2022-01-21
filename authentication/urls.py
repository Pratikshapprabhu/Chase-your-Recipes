from django.contrib import admin
from django.urls import path,include
from .import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path("perform_register/",views.perform_register,name="perform_register"),
    path('render_login', views.render_login , name="render_login"),
    path("perform_login/",views.perform_login,name="perform_login"),
    path("perform_logout/",views.perform_logout,name="perform_logout"),
    path("home/",RedirectView.as_view(url='<cookbook_url>'),name="home"),
    path('search/', RedirectView.as_view(url='<cookbook_url>'), name = 'search'),
    path("recipe_view/<slug:recipe_name>", RedirectView.as_view(url='<cookbook_url>'), name = 'recipe_view'),
    ]