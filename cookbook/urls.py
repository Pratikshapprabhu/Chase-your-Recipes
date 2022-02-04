from django.urls import path, re_path
from . import views


app_name = "cookbook"

urlpatterns = [
     path('search/', views.search, name = 'search'),
     path('sync/',views.sync, name = 'sync'),
     path("recipe_view/<int:pk>", views.recipe_view, name = 'recipe_view'),
     path("save_recipe/", views.save_recipe, name = 'save_recipe'),
     path("remove_recipe/", views.remove_recipe, name = 'remove_recipe'),
     path("saved-recipes/", views.saved_recipes, name = 'saved_recipes'),
]
