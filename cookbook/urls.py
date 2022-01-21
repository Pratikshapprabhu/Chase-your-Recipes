from django.urls import path, re_path
from . import views


app_name = "cookbook"

urlpatterns = [
     path('search/', views.search, name = 'search'),
     path('sync/',views.sync, name = 'sync'),
     path("home/",views.home,name="home"),
     path("recipe_view/<slug:recipe_name>", views.recipe_view, name = 'recipe_view'),
]
