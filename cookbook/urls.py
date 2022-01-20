from django.urls import path
from . import views

app_name = "cookbook"

urlpatterns = [
     path('search/', views.search, name = 'search'),
     path('sync/',views.sync, name = 'sync'),
     path("home/",views.home,name="home"),
]
