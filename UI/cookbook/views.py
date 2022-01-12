from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def search(request):
    var = request.POST.get("searchbar")
    return HttpResponse(f"Display success:{var}")
    
