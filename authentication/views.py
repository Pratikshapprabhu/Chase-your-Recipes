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
