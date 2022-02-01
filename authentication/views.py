from urllib import response
from django.contrib.auth import forms
from django.forms.forms import Form
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.urls import reverse
from django.contrib import messages
from cookbook.models import RecipeIndex
from math import ceil

from .forms import UserRegisterForm


    
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        return render(request,"register.html", context={"form": form})
    else:
        form=UserRegisterForm()
        return render(request,"register.html", context={"form":form})

def perform_register(request):
    if request.method  != "POST":
        return HttpResponse("Method not allowed")
    else:
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user_obj1=authenticate(request,username=username,email=email,password=password)
        if user_obj1 is not None:
            login(request,user_obj1)
            return redirect(response, 'search_result.html')
        else:
            messages.error (request,"User already exists")
            return HttpResponseRedirect("login")

def login(request):
    context={}
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user_obj=authenticate(request,username=username,password=password)
        if user_obj is not None:
            login(request,user_obj)
            return HttpResponseRedirect(reverse("admin_dashboard"))
        else:
            messages.error (request,"Username or Password is invalid")
            return render(request, "login.html", context=context)
    else:
        return render(request,"login.html",  context=context) 

def perform_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
