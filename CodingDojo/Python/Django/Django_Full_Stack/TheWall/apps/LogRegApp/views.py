from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
from .models import *



def index(request):
    print('================This is the Login Index======================')
    return render(request, 'index.html')

def register(request):
    if User.objects.registration_validator(request.POST, request):
        isValid = True
        # user = User.objects.get(email=request.POST['email'])
        return redirect('/success')
    else:
        isValid = False
        return redirect('/')

def success(request):
    return render(request, 'index.html')

def login(request):
    if User.objects.user_exists(request.POST, request):
        isValid = True
        user = User.objects.get(email=request.POST['email']) # Usser.get gets one object. User.get gets an array of users
        request.session['email'] = user.email
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
        # print(request.session['email'])
        # print(request.session['first_name'])
        return redirect('/wall')
    else:
        isValid = False
        return redirect('/')
