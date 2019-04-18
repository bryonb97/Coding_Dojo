from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
from .models import *



def index(request):
    return render(request, 'index.html')

def register(request):
    if User.objects.registration_validator(request.POST, request):
        isValid = True
        return redirect('/success')
    else:
        isValid = False
        return redirect('/')

def success(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'success.html', context)

def login(request):
    if User.objects.user_exists(request.POST, request):
        isValid = True
        return redirect('/success')
    else:
        isValid = False
        return redirect('/')
