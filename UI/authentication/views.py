from django.contrib.auth import forms
from django.forms.forms import Form
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.urls import reverse
from django.contrib import messages
from authentication.models import registered_user


# Create your views here.
def index(request):
    return render(request,"index.html")
    
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        emailid = request.POST['emailid']
        password = request.POST['psw1']
        savedata = registered_user(username = username, emailid = emailid, password = password)
        savedata.save()
        print("Data saved successfully")
    return render(request,"register.html")

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
            return HttpResponseRedirect(reverse("admin_dashboard"))
        else:
            messages.error (request,"User already exists")
            return HttpResponseRedirect("render_login")

def render_login(request):
    return render(request,"login.html") 

def perform_login(request):
        username=request.POST.get("username")
        password=request.POST.get("password")
        user_obj=authenticate(request,username=username,password=password)
        if user_obj is not None:
            login(request,user_obj)
            return HttpResponseRedirect(reverse("admin_dashboard"))
        else:
            messages.error (request,"Username or Password is invalid")
            return HttpResponseRedirect("/")

def admin_dashboard(request):
    return render(request,"admin_dashboard.html")

def perform_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


